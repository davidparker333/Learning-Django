from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=120) # max_length required
    body = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)