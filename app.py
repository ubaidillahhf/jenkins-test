from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Check triggering webhook lagi v12!!!!'