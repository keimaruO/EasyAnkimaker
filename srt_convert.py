import re

def convert_timecode(timecode):
    hours, minutes, seconds, milliseconds = re.split("[:.,]", timecode)
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return total_seconds

with open("G:/Scripts/推し英単語/29_桃鈴ねね.srt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

with open("G:/Scripts/推し英単語/output_.srt", "w", encoding="utf-8") as output_file:
    for line in lines:
        match = re.match(r"(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)", line)
        if match:
            start_timecode = convert_timecode(match.group(1))
            end_timecode = convert_timecode(match.group(2))
            output_file.write(f"{start_timecode} --> {end_timecode}\n")
        else:
            output_file.write(line)
