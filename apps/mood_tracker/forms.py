from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Mood


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MoodForm(ModelForm):
    class Meta:
        model = Mood
        fields = ['emotion', 'day_date', 'day_time', 'reason',
                  'reaction', 'reaction_rate']
