from flask import Flask

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    return """
<Response>
    <Say>Hello from my server</Say>
</Response>
"""

if __name__ == "__main__":
    app.run(port=5000)