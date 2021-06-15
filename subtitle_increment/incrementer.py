import datetime
from _collections import OrderedDict
import argparse

def increment_subtitles(file_name: str, seconds: float, ms: float, new_file_name:str):
    """

    :param file_name:
    :param seconds:
    :param ms
    :param new_file_name:
    :return:
    """
    increment_amount = datetime.timedelta(seconds=seconds, milliseconds=ms)
    subtitle_file = open(file_name, "r", encoding='utf8')
    subtitle_dict = OrderedDict()
    while True:
        caption_num = subtitle_file.readline().replace("\n", "")
        if not caption_num:
            break
        timerange_raw = subtitle_file.readline().replace("\n", "")
        timerange_split = timerange_raw.split(" --> ")
        start_dialogue = datetime.datetime.strptime(timerange_split[0], '%H:%M:%S,%f')
        end_dialogue = datetime.datetime.strptime(timerange_split[-1], '%H:%M:%S,%f')

        # read in variable range of dialogue lines
        dialogue_lines = []
        current_line = subtitle_file.readline().replace("\n", "")
        while current_line:
            dialogue_lines.append(current_line)
            current_line = subtitle_file.readline().replace("\n", "")
        subtitle_dict[caption_num] = {"start": start_dialogue,
                                      "end": end_dialogue,
                                      "lines": dialogue_lines}

    print(subtitle_dict)
    new_subtitle_file = open(new_file_name, "w", encoding='utf8')
    for caption_num in subtitle_dict.keys():
        new_subtitle_file.write("%s\n"%caption_num)
        new_start = subtitle_dict[caption_num]["start"] + increment_amount
        new_start_string = new_start.strftime('%H:%M:%S,%f')[:-3]
        new_end = subtitle_dict[caption_num]["end"] + increment_amount
        new_end_string = new_end.strftime('%H:%M:%S,%f')[:-3]

        new_subtitle_file.write("%s --> %s\n" % (new_start_string, new_end_string))
        for line in subtitle_dict[caption_num]["lines"]:
            new_subtitle_file.write("%s\n" % line)
        new_subtitle_file.write("\n")
    new_subtitle_file.close()
