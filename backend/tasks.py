import os, sys, subprocess
from celery import Celery

config = dict(
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',
    CELERY_IGNORE_RESULT = False,
    CELERYD_CONCURRENCY = 2,
    CELERY_TRACK_STARTED = True
)

REDIS_SERVER = os.environ['REDIS_JOBQ_SERVICE_HOST']

app = Celery('tasks',
    backend='redis://%s'%REDIS_SERVER,
    broker='redis://%s'%REDIS_SERVER)
app.conf.update(config)

@app.task
def test(ctx):
    print('Hello!')

