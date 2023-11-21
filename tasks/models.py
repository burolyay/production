from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
