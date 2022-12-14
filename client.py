import socketio

sio = socketio.Client()

@sio.on('connect')
def connect():
    print("connected to server")

@sio.on('disconnect')
def disconnect():
    print("disconnect from server")

# @sio.event('message')
# def message(data):
#     print('message recieved ', data)


if __name__ == '__main__':
    sio.connect('http://localhost:5000')

    i = 0
    while True:
        sio.emit('hello', i)
        print('emitted message', i)
        i += 1
