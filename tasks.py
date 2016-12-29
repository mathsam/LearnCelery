from celery import Celery

app = Celery('tasks', broker='amqp://junyic:0714@node00:5672/myvhost',
        backend='rpc://')


import time

@app.task
def add(x, y):
    time.sleep(5)
    return x + y
