from django.contrib import admin

from .models import UserProfile, Achievement

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'surname', 'deleted')
    list_filter = ('name', 'surname')
    search_fields = ['name', 'surname']


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description')
    list_filter = ('title',)
    search_fields = ['title']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Achievement, AchievementAdmin)
