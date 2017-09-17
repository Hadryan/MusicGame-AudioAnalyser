from unicodedata import normalize
from flask import Flask, request
from util import security, rhythm
import ConfigParser
import os

UPLOAD_FOLDER = '/home/ubuntu/audio_repo'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def hello_world():
    return "Hello!!!!"

@app.route('/file', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        raw_file_name_uft8 = normalize('NFKD', file.filename).encode('utf-8', 'strict').decode('utf-8')
        filename = security.secure_filename(raw_file_name_uft8)
        path_name = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path_name)
        return path_name
    return "hoops, there may be some error"

@app.route('/rhythm', methods=['POST'])
def audio_rhythm_info():
    filename = request.form['filename']
    return str(rhythm.rhythm_extractor(filename))

def get_port():
    config = ConfigParser.ConfigParser()
    config.read(os.path.abspath('..') + '/config.ini')
    port = config.get("remote", "port")
    return int(port)

if __name__ == '__main__':
    # modify the port dynamically
    remote_port = get_port()
    app.run(host='0.0.0.0', port=remote_port)
