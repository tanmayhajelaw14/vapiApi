import os

os.environ["PATH"] += r";D:\ffmpeg-8.1.1-essentials_build\bin"

import whisper

model =  whisper.load_model("base")
result = model.transcribe("real_sample.wav")

print(result["text"])