from django.db import models

# Create your models here.


class Diary(models.Model):
    day_date = models.DateField()
    entry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Diary entry - {self.day_date}"
