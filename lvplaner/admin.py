from django.contrib import admin
from .models import Major, Subject, Student, Course

# Register your models here.
admin.site.register(Major)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Course)

