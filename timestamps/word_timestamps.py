import os
import sys
import wave
import json

from vosk import Model, KaldiRecognizer, SetLogLevel
# !pip install vosk

SetLogLevel(0)


# path to vosk model downloaded from
# https://alphacephei.com/vosk/models
def Recognizer(audio_path:str):
    model_path = os.path.join(sys.path[0],"../vosk-model-small-en-us-0.15")

    if not os.path.exists(model_path):
        print(f"Please download the model from https://alphacephei.com/vosk/models and unpack as {model_path}")
        sys.exit()

    print(f"Reading your vosk model '{model_path}'...")
    model = Model(model_path)
    print(f"'{model_path}' model was successfully read")

    # name of the audio file to recognize
    # audio_filename = "../audio/speech_recognition_systems.wav"
    audio_filename = os.path.join(sys.path[0],audio_path)

    if not os.path.exists(audio_filename):
        print(f"File '{audio_filename}' doesn't exist")
        sys.exit()


    print(f"Reading your file '{audio_filename}'...")
    wf = wave.open(audio_filename, "rb")
    print(f"'{audio_filename}' file was successfully read")


    # check if audio is mono wav
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit()
    results = []


    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)



    # recognize speech using vosk model
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)

    part_result = json.loads(rec.FinalResult())
    results.append(part_result)
    return results

