from django.db import models

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()
