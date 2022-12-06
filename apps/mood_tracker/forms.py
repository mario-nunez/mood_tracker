from django.forms import ModelForm

from .models import Mood


class MoodForm(ModelForm):
    class Meta:
        model = Mood
        fields = ['emotion', 'day_date', 'day_time', 'reason',
                  'reaction', 'reaction_rate']
