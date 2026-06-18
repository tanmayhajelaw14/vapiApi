# import asyncio
# import json
# import websockets


# async def handle(ws):
#     print("Client Connected")

#     async for message in ws:
#         print("Received Message")
#         print(message)


# async def main():
#     server = await websockets.serve(
#         handle,
#         "0.0.0.0",
#         5001
#     )

#     print("WebSocket Server Running on Port 5001")

#     await server.wait_closed()


# asyncio.run(main())