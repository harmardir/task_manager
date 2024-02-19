from django.db import models
from tasks.tasks import print_message

class Task(models.Model):
    message = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
        print_message.delay(self.message)

