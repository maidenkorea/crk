import socketio
import asyncio


username = 'peanits'
server_dest = 'http://127.0.0.1:8000'
sio = socketio.AsyncClient()


@sio.event
async def connect():
    await sio.emit('client_id', username)

@sio.on('victim_event')
async def victim_event(data):
    print(data)

async def send_event(car_id, event_type=None):
    await sio.emit('pvp_event', data={'victim': car_id, 'event': event_type})

async def main():
    await sio.connect(server_dest)
    await send_event('peanits', 'test')
    await sio.wait()
    

asyncio.run(main())