import argparse
from subtitle_increment.incrementer import increment_subtitles
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Increment subtitle file')
    parser.add_argument("file_name",  type = str, help = "Subtitle file to increment")
    parser.add_argument('--seconds', "-s", type=float,
                        help='seconds to increment dialogue', default=0)
    parser.add_argument('--milliseconds', "-ms", type=float,
                        help='milliseconds to increment dialogue', default=0)
    parser.add_argument("--output", "-o",type=str, default="new_subtitle.srt", help = "output file name of incremented subtitle. Defaults to new_subtitle.srt" )

    args = parser.parse_args()

    file_name = args.file_name
    new_file_name = args.output
    seconds = args.seconds
    ms = args.milliseconds

    increment_subtitles(file_name, seconds, ms, new_file_name)
