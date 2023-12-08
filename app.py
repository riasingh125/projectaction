from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    timestamp = data.get('timestamp', None)
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['timestamp'] = timestamp
    socketio.emit('message', data)  # Emit the message with timestamp

if __name__ == '__main__':
    socketio.run(app)
