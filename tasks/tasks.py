from celery import shared_task
import time

@shared_task
def print_message(message):
    time.sleep(5)  # Simulate some long-running task
    print(message)
