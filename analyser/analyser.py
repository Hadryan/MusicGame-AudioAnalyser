from flask import Flask
import ConfigParser
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello!"


if __name__ == '__main__':
    # modify the port dynamically
    config = ConfigParser.ConfigParser()
    config.read(os.path.abspath('..') + '/config.ini')
    remote_port = config.get("remote", "port")

    app.run(host='0.0.0.0', port=int(remote_port), debug=True)
