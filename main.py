from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    url_for('static', filename='style.css')

    return render_template('index.html')

@app.route('/hello')
def hello():
    url_for('static', filename='style.css')

    return "Hello page"
