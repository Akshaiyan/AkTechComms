from flask import Flask, render_template,request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    #user = request.args.get['username']
    return render_template('index.html')
@app.route('/chat')
def sessions():
    user = request.args.get('username')
    return render_template('session.html',user=user)

def messageReceived():
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)