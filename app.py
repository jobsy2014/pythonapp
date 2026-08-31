from flask import Flask
import flask as FL
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from GitHub Actions!"

if __name__ == "__main__":
    app.run()