import asyncio
import json
import websockets


async def handle(ws):

    print("Client Connected")

    async for message in ws:

        event = json.loads(message)

        event_type = event.get("event")

        print(f"Event Type: {event_type}")

        if event_type == "connected":
            print("Exotel Connected")

        elif event_type == "start":
            print("Call Started")

        elif event_type == "media":

            payload = event["media"]["payload"]

            import base64

            audio_bytes = base64.b64decode(payload)

            with open("audio.raw", "ab") as f:
                f.write(audio_bytes)

            print(f"Bytes Received: {len(audio_bytes)}")

        elif event_type == "stop":
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