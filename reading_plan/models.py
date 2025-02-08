from django.db import models

# Create your models here.
class ReadingPlan(models.Model):
    date = models.DateField()
    old_testament = models.CharField(max_length=100)
    new_testament = models.CharField(max_length=100)
    psalm = models.CharField(max_length=100)


from django.http import JsonResponse
from .api_request import fetch_bible_chapter  # Assuming fetch_bible_chapter is in services.py


