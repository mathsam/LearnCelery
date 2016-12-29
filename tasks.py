from celery import Celery

app = Celery('tasks', broker='pyamqp://guest:guest@node00//',
        backend='pyamqp://guest:guest@node00')


import time

@app.task
def add(x, y):
    time.sleep(5)
    return x + y
