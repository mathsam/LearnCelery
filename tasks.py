from celery import Celery
import celeryconfig
import numpy as np

app = Celery('tasks')
app.config_from_object(celeryconfig)


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

import random


@app.task(bind=True, default_retry_delay=10, max_retries=10)
def test_retry(self, upper_limit):
    try:
        randint = random.randint(0, upper_limit)
        if randint != 0:
            raise RuntimeError('n is %d' %randint)
        else:
            print('Success')
            return 0
    except RuntimeError as e:
        raise self.retry(exc=e, countdown=2**self.request.retries)

sum = app.task(np.sum)
