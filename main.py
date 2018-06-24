from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-file', methods=['POST', 'GET'])
def send_file():
    if request.method == 'POST':

        f = request.files['archivo']

        f.save('./files/' + secure_filename(f.filename))

        return 'Se ha subido con exito!'
    elif request.method == 'GET':
        return render_template('send-file.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
