from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="event_images", blank=True, null=True)
    location = models.CharField(max_length=255)
    hosted_time = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    hosted_by = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
