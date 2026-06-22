import asyncio
import websockets
import json
import base64

# fake_audio = base64.b64encode(
#     b"hello"
# ).decode()

with open("real_sample.wav","rb") as f:
    audio_data=f.read()

print(f"Audio Data Size: {len(audio_data)} bytes")

chunk = audio_data[:320]
print(f"Chunk Size: {len(chunk)} bytes")

encoded_chunk = base64.b64encode(chunk).decode()
print(type(encoded_chunk))
print(f"Encoded Chunk Size: {len(encoded_chunk)} characters")

print(len(audio_data) // 320)

total_chunks = len(audio_data) // 320

async def test():

    uri = "ws://localhost:5001"

    async with websockets.connect(uri) as ws:

        await ws.send(
            json.dumps({
                "event": "connected"
            })
        )

        await ws.send(
            json.dumps({
                "event": "start"
            })
        )

        for i in range(total_chunks):
            start = i*320
            end = (i+1) * 320
            chunk = audio_data[start:end]
            encoded_chunk = base64.b64encode(chunk).decode()
            print(f"Chunk {i}: "f"start={start}, "f"end={end}, "f"size={len(chunk)}")
            await ws.send(
                json.dumps({
                    "event": "media",
                    "media": {
                        "payload": encoded_chunk
                    }
                })
            )

        await ws.send(
            json.dumps({
                "event": "stop"
            })
        )


asyncio.run(test())