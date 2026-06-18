import asyncio
import websockets
import json
import base64

fake_audio = base64.b64encode(
    b"hello"
).decode()


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

        await ws.send(
            json.dumps({
                "event": "media",
                "media": {
                    "payload": fake_audio
                }
            })
        )

        await ws.send(
            json.dumps({
                "event": "stop"
            })
        )


asyncio.run(test())