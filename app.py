# Import necessary modules
from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import datetime

# Create Flask app and SocketIO instance
app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# SocketIO event handler for incoming messages
@socketio.on('message')
def handle_message(data):
    # Get timestamp from data, or generate if not present
    timestamp = data.get('timestamp', None)
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['timestamp'] = timestamp

    # Emit the message with timestamp to all connected clients
    socketio.emit('message', data)

# Run the application with SocketIO
if __name__ == '__main__':
    socketio.run(app)
