from celery import Celery

process = Celery('celery_task', broker= "redis://redis-store:6379/0", backend="redis://redis-store:6379/0")


name = "hello"

age = "25"

task = process.send_task('add', kwargs={"name": name, "age":age})

print(task.id)