import asyncio
from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp', async_handlers=True)
app = web.Application()
sio.attach(app)

@sio.on('connect')
def connect(sid, environ):
    print("connected: ", sid)

@sio.on('hello')
async def message(sid, data):
    print("hello ", data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect: ', sid)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=5000)
