import word_timestamps
import os,sys
def Recognizer(i):
    audio_path=f'../media/audio/media{i}.wav'
    result=word_timestamps.Recognizer(audio_path)
    result_array=[]
    for i in result:
        if len(i) == 1:
            continue
        for j in i['result']:
            result_array.append(j)

    return result_array