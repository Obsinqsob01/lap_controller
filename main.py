from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola mundo!"

@app.route('/hello')
def hello():
    return "Hello page"
