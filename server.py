import flask
import json

from flask import Flask, abort
from flask import request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)


@app.route('/api/devices', methods=['GET'])
def devices():
    f = open("devices.txt", "r")
    q = f.read()
    return q
import datetime, threading


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 2528)