from .tg_handler import msg
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Zero Sum: Home"

def process_message(data):
    """Function to process and print the received data."""
    print(f"Processing message: {data}")
    asyncio.run(msg(data))
    app.logger.info(f"Processed message: {data}")  # Log it to the file

@app.route("/data", methods=["POST"])
def receive_data():
    """Receive data from POST request and pass it to process_message."""
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    process_message(data)  # Pass data to the function

    return jsonify({"status": "Message received and processed"}), 200

def launch_app():
    app.run(host="0.0.0.0", port=5000)
