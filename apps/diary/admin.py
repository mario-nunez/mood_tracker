from django.contrib import admin

from .models import Diary

# Register your models here.


class DiaryAdmin(admin.ModelAdmin):
    list_display = ('day_date', 'entry')


admin.site.register(Diary, DiaryAdmin)
