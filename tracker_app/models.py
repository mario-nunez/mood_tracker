from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profpic.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class MoodTracker(models.Model):
    DAY_PART_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]
    emotion = models.CharField(max_length=30)
    day_date = models.DateField()
    day_time = models.TimeField()
    day_part = models.CharField(max_length=10, choices=DAY_PART_CHOICES)
    reason = models.TextField()
    reaction = models.TextField()
    reaction_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.emotion}-{self.day_date}"
