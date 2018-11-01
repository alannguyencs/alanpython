import pafy
from pydub import AudioSegment
import os


def get_time(string_time):
    [minute, second] = string_time.split(':')
    minute, second = int(minute), int(second)
    return (minute * 60 + second) * 1000

def audio_split(origin_file, result_file, time_period):
    sound = AudioSegment.from_file(origin_file)
    result_sound = sound[0:0]

    for period in time_period:
        start_period, end_period = get_time(period[0]), get_time(period[1])
        result_sound += sound[start_period : end_period]

    result_sound.export((result_file), format="mp3")

#=====================================================================================================
origin_path = "D:/Cambridge ielts 8/CD1/"
result_path = "C:/Users/tnguyenhu2/Dropbox/English/ielts/audio/"

origin_file = origin_path + "Track 5.mp3"
result_file = result_path + "8_5.mp3"

time_period = [("2:20", "4:05"), ("4:49", "7:13")]
audio_split(origin_file, result_file, time_period)