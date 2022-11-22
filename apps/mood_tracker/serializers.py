from rest_framework import serializers
from .models import Mood


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'


class MoodsDaySerializer(serializers.ModelSerializer):
    total_moods = serializers.IntegerField()
    day_avg_rate = serializers.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        model = Mood
        fields = ['day_date', 'day_week', 'total_moods', 'day_avg_rate']
