from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
