from django.db import models

# Create your models here.


class Lesson(models.Model):
    TOPIC_CHOICES = [
        ('Career', 'Career'),
        ('Relationships', 'Relationships'),
        ('Life', 'Life'),
    ]
    topic = models.CharField(max_length=30, choices=TOPIC_CHOICES)
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lesson-{self.topic}-{self.category}-{self.title}"
