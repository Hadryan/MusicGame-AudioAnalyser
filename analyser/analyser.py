import ConfigParser
import os
from flask import Flask, request
from util import rhythm, file, variables

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = variables.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def hello_world():
    return "Hello!!!!"

@app.route('/file', methods=['POST'])
def upload_file():
    music_file = request.files['file']
    return str(file.file_save(music_file=music_file))

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
