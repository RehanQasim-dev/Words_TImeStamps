from pydub import AudioSegment
import sys,os
for i in range(1,6):
    sound=AudioSegment.from_mp3(sys.path[0]+f'/media/rawaudio/media{i}.mp3')
    sound.export(sys.path[0]+f'/media/audio/media{i+1}.wav',format='wav')