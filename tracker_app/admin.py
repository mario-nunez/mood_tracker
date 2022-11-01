from django.contrib import admin

from .models import MoodTracker, Client

# Register your models here.

admin.site.register(MoodTracker)
admin.site.register(Client)
