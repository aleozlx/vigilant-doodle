import os, sys
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
app = Flask(__name__)
import json

err = lambda d: (json.dumps(dict(status='err', msg=d)), 500)
ok = lambda d: json.dumps(dict(status='ok', data=d))
pending = lambda d: json.dumps(dict(status='pending', msg=d))

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route('/version')
def version():
    return ok('v0.1.0')

