from celery import Celery
import time

app = Celery()

@app.task

def add (**kwargs):
    x= kwargs.get('name')
    y= kwargs.get('age')
    print("My name is",x,"My age is",y)
    time.sleep(5)

    return("Success")