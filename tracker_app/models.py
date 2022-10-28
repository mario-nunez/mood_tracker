from email.policy import default
from random import choices
from django.db import models

# Create your models here.


class MoodRegister(models.Model):
    DAY_PART_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]
    emotion = models.CharField(max_length=20)
    day_date = models.DateField()
    day_time = models.CharField(choices=DAY_PART_CHOICES)
    reason = models.CharField(max_length=200)
    reaction = models.CharField(max_length=200)
    reaction_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
