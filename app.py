from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)

socketio = SocketIO(app)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    print(f'Mensagem recebida via chat: {msg}')
    emit('message', msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
