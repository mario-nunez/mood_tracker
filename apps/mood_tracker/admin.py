from django.contrib import admin

from .models import Mood

# Register your models here.


class MoodAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'emotion', 'day_date', 'day_time',
                    'reaction_rate')
    list_filter = ('emotion', 'day_date')
    search_fields = ['emotion']
    ordering = ['-day_date']


admin.site.register(Mood, MoodAdmin)
