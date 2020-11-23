import asyncio
import websockets

async def event():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        name = input("T/F? ")
        await websocket.send(name)

asyncio.get_event_loop().run_until_complete(event())
