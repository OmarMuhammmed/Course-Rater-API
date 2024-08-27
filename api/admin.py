from django.contrib import admin
from .models import *
# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ['course', 'user', 'stars']
    list_filter = ['course']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'category', 'duration']
    list_filter = ['category']
    search_fields = ['course','instructor', 'category']


admin.site.register(Rating,RatingAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Instructor)
