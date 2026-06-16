from flask import Flask, request
from dataclasses import dataclass
import marshmallow_dataclass

app = Flask(__name__)

@dataclass
class Message:
    type: str
    transcript: str | None = None

MessageSchema = marshmallow_dataclass.class_schema(Message)

@app.route("/webhook", methods=["POST"])
def webhook():

    message = MessageSchema(unknown="exclude").load(request.json["message"])

    print("\nEvent Type:", message.type)

    if message.transcript:
        print("Transcript:", message.transcript)

    return {"success": True}

app.run(host="0.0.0.0",port=5000)