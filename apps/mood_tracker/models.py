import calendar

from django.core.validators import MaxValueValidator
from django.db import models

from .constants import MAX_REACTION_RATE, MORNING, AFTERNOON, EVENING, NIGHT
from apps.core.models import UserProfile


# Create your models here.

class Mood(models.Model):
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.CASCADE)
    emotion = models.CharField(max_length=30)
    day_date = models.DateField()
    day_week = models.CharField(max_length=10, blank=True)
    day_time = models.TimeField()
    day_part = models.CharField(max_length=10, blank=True)
    reason = models.TextField()
    reaction = models.TextField()
    reaction_rate = models.PositiveIntegerField(
                           validators=[MaxValueValidator(MAX_REACTION_RATE)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_day_part(self, parts):
        for part in parts:
            if self.day_time >= part['start'] and self.day_time <= part['end']:
                self.day_part = part['value']
                return
        # if not in any range it's night
        self.day_part = part['value']

    def save(self, *args, **kwargs):
        # overwrite save method to add automatically some fields
        self.day_week = calendar.day_name[self.day_date.weekday()]
        parts = [MORNING, AFTERNOON, EVENING, NIGHT]
        self._get_day_part(parts)
        super(Mood, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return (f"{self.user_profile}-{self.emotion}-"
                f"{self.day_date}-{self.day_time}")
