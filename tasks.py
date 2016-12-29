from celery import Celery
import numpy as np

app = Celery('tasks', broker='amqp://junyic:0714@node00:5672/myvhost',
        backend='rpc://')


import time

@app.task
def add(x, y):
    return x + y

@app.task
def exhaust_ram(s, t):
    print('Consume %f Mb RAM' %(s*8./1024/1024))
    np.zeros(s)+1
    if t>0:
        time.sleep(t)
    return None
