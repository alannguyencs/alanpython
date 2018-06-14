#https://github.com/mps-youtube/pafy
import pafy
from pydub import AudioSegment
import os

url = "https://www.youtube.com/watch?v=pLgXDWMD7dg&t=451s"
video = pafy.new(url)

bestaudio = video.getbestaudio()
bestaudio.download()


print (video.title)
# AudioSegment.from_file((video.title + ".m4a")).export((video.title + ".mp3"), format="mp3")
# sound = AudioSegment.from_file((video.title + ".mp3"))
sound = AudioSegment.from_file((video.title + "." + bestaudio.extension))


episode_sound = sound

#watch the clip on youtube to determine the duration to segment
start = (1 * 60 + 20) * 1000
end = start + 15 * 1000
# end = (1 * 60 + 35) * 1000

episode_sound = sound[start:end]


# episode_sound = episode_sound


# episode_sound.export((video.title + ".mp3"), format="mp3")
episode_sound.export(("6.mp3"), format="mp3")
os.remove((video.title + "." + bestaudio.extension))


"""
0:31 - 0:44 con buom xua
0:45 - 1:00 ca phe miet vuon
1:00 - 1:15: con mua ngang qua
1:15 - 1:30: nhu mot giac mo
1:30 - 1:45: nang kieu lo buoc
"""