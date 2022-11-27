from django.contrib import admin

from .models import Lesson

# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'category', 'title')


admin.site.register(Lesson, LessonAdmin)
