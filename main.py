from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.update(
	UPLOAD_FOLDER = "files"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-file', methods=['POST', 'GET'])
def send_file():
    if request.method == 'POST':

        for file in request.files.getlist('file[]'):
            file.save('./files/' + secure_filename(file.filename))

        return 'The upload has finished successfully!'
    elif request.method == 'GET':
        return render_template('send-file.html')

@app.route('/change-wallpaper', methods=['POST', 'GET'])
def change_wallpaper():
    """Page for wallpaper uploading"""
    if request.method == 'POST':
        file = request.files['wallpaper']
        file.save('./files/background.jpg')
        return redirect("/")

    return render_template('change-wallpaper.html')

@app.route('/files/<filename>')
def uploaded_file(filename):
    """Return file from directory"""
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
