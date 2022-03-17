from celery import Celery
from time import sleep

# result backend is actually necessary to get the result
celery_app = Celery(
    "tasks", broker="redis://redis:6379", CELERY_RESULT_BACKEND="redis://redis:6379"
)


@celery_app.task
def slow_reverse(text):
    sleep(5)
    return text[::-1]
