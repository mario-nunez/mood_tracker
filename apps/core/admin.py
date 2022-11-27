from django.contrib import admin

from .models import UserProfile, Achievement

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'deleted')


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Achievement, AchievementAdmin)
