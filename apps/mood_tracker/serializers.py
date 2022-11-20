from rest_framework import serializers
from .models import Mood


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'


class MoodsDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['day_date', 'day_week', 'reaction_rate']
