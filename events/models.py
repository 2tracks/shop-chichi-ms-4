from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    date_and_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
