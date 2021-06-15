# Overview
Command changes the timestamps of an srt file using a constant time increment. This can be useful if an srt file lags behind 
or in front of a movie you want to watch
## Installation
```
pip install subtitle-increment
```

## Usage
```
python -m subtitle_increment --help
usage: __main__.py [-h] [--seconds SECONDS] [--milliseconds MILLISECONDS]
                   [--output OUTPUT]
                   file_name

Increment subtitle file

positional arguments:
  file_name             Subtitle file to increment

optional arguments:
  -h, --help            show this help message and exit
  --seconds SECONDS, -s SECONDS
                        seconds to increment dialogue
  --milliseconds MILLISECONDS, -ms MILLISECONDS
                        milliseconds to increment dialogue
  --output OUTPUT, -o OUTPUT
                        output file name of incremented subtitle. Defaults to
                        new_subtitle.srt
```

## Example
```
python -m subtitle_increment La.Notte.1961.1080p.BluRay.x264-PublicHD.ita-Italian.srt -s -5 -ms -100 --output new_subtitles.srt
```

This command decrements all the dialogue in the subtitle file by 5 seconds and 100 milliseconds. The output srt file is
new_subtitle.srt

## Quirks
* Program assumes utf-8 encoding.
* No Unit Tests since code is brutally simple