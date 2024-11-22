import socketio
# to run server type
# uvicorn --reload app:app


sio = socketio.AsyncServer(async_mode = 'asgi')
app = socketio.ASGIApp(sio, static_files={
    '/':'.public/'
})
users = { }


@sio.event
async def connect(sid, environ):
    print(sid, 'connected')

@sio.event
async def disconnect(sid):
    users.pop(sid, None)
    print(sid, 'disconnected')
    print(users)

@sio.on('client_id')
async def client_id(sid, data):
    users[sid] = data
    print(users)

@sio.on('pvp_event')
async def pvp_event(sid, data_in):
    victim = [key for key, value in users.items() if value == data_in['victim']][0]
    await sio.emit('victim_event', to=victim, data=data_in['event'])

async def car_event(car_id):
    sio.emit('car_event', to=car_id)