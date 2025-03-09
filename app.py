from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

chat_history = [] 

@app.route("/")
def index():
    return render_template("chat.html")

@socketio.on("connect")
def handle_connect():
    socketio.emit("chat_history", chat_history) 

@socketio.on("message")
def handle_message(msg):
    chat_history.append(msg)
    socketio.emit("message", msg)  

if __name__ == "__main__":
    socketio.run(app, debug=True)
