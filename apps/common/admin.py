from django.contrib import admin

from .models import UserProfile, Achievement

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Achievement)
