from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-file', methods=['POST', 'GET'])
def send_file():
    if request.method == 'POST':
        print("pst method")
    elif request.method == 'GET':
        return render_template('send-file.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
