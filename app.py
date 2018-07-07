from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    HOME
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8787, debug=True)

