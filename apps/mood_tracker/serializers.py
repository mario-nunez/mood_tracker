from rest_framework import serializers
from .models import MoodTracker


class MoodTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodTracker
        fields = '__all__'
