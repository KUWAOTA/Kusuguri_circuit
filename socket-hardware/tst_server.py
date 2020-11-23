
import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    if bool(name):
        print("test")

start_server = websockets.serve(hello, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
