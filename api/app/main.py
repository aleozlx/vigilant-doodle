# pylint: disable=import-error,no-name-in-module
import os, sys
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
app = Flask(__name__)
import json
from tasks import task_hello
import time

err = lambda d: (json.dumps(dict(status='err', msg=d)), 500)
ok = lambda d: json.dumps(dict(status='ok', data=d))
pending = lambda d: json.dumps(dict(status='pending', msg=d))

@app.route('/version')
def version():
    return ok('v0.1.0')

def test_redis_jobq():
    task = task_hello.delay()
    task_id = task.id
    r = task_hello.AsyncResult(task_id)
    while r.state not in ['SUCCESS', 'FAILURE']:
        time.sleep(2)
    return ok(dict(
        task_id = task_id,
        state = r.state
    ))

@app.route('/t/<test_fn>', methods=['POST'])
def test(test_fn):
    if test_fn.startswith('test_'):
        return globals()[test_fn]()
    else:
        return err('test case not found')
