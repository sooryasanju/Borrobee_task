from django.db import models
from datetime import date
import datetime

# Create your models here.

class Reminder_mod(models.Model):
    name=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    def __str__(self):
        return self.name
