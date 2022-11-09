import calendar

from django.db import models

from .constants import MORNING, AFTERNOON, EVENING, NIGHT


# Create your models here.

class MoodTracker(models.Model):
    emotion = models.CharField(max_length=30)
    day_date = models.DateField()
    day_week = models.CharField(max_length=10, blank=True)
    day_time = models.TimeField()
    day_part = models.CharField(max_length=10, blank=True)
    reason = models.TextField()
    reaction = models.TextField()
    reaction_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_day_part(self, parts):
        for part in parts:
            if self.day_time >= part['start'] and self.day_time <= part['end']:
                self.day_part = part['value']
                return

    def save(self, *args, **kwargs):
        # overwrite save method to add automatically some fields
        self.day_week = calendar.day_name[self.day_date.weekday()]
        parts = [MORNING, AFTERNOON, EVENING, NIGHT]
        self.get_day_part(parts)
        super(MoodTracker, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.emotion}-{self.day_date}"
