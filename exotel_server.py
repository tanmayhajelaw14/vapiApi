import base64
import asyncio
import json
import websockets
import os
import whisper

audio_buffer = bytearray()

print("Loading Whisper Model...")
model = whisper.load_model("base")
print("Whisper Model Loaded")
os.environ["PATH"] += r";D:\ffmpeg-8.1.1-essentials_build\bin"

async def handle(ws):

    global audio_buffer

    print("Client Connected")

    async for message in ws:

        event = json.loads(message)

        event_type = event.get("event")

        print(f"Event Type: {event_type}")

        if event_type == "connected":
            print("Exotel Connected")

        elif event_type == "start":
            audio_buffer.clear()
            print("Call Started")

        elif event_type == "media":

            payload = event["media"]["payload"]

            audio_bytes = base64.b64decode(payload)

            audio_buffer.extend(audio_bytes)

            print(f"Chunk: {len(audio_bytes)} bytes | "f"Buffer Size: {len(audio_buffer)} bytes")

        elif event_type == "stop":
            with open("received_audio.wav", "wb") as f:
                f.write(audio_buffer)
                
            
            result = model.transcribe("received_audio.wav")
            print(result["text"])
            print(f"Final Buffer Size: {len(audio_buffer)} bytes")
            print(audio_buffer[:20])
            print(os.path.getsize("received_audio.wav"))
            print("Call Ended")


async def main():

    server = await websockets.serve(
        handle,
        "0.0.0.0",
        5001
    )

    print("Server Running")

    await server.wait_closed()


asyncio.run(main())