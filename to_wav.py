from pydub import AudioSegment
import sys,os
for i in range(3,43):
    sound=AudioSegment.from_mp3(sys.path[0]+f'/media/rawaudio/media{i}.mp3')
    sound.export(sys.path[0]+f'/media/audio/media{i}.wav',format='wav')