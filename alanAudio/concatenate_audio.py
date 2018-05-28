from pydub import AudioSegment



sound1 = AudioSegment.from_file("1.mp3")
sound2 = AudioSegment.from_file("2.mp3")

sound = sound1 + sound2

sound.export("result.mp3", format="mp3")

