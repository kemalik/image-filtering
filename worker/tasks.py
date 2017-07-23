from celery import Celery

app = Celery('tasks', broker='amqp://localhost', backend='amqp://localhost')


@app.task(name='apply_filter')
def apply_filter(image_id, filter_type):
    return image_id, filter_type
