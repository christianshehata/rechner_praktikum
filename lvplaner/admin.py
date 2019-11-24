from django.contrib import admin
from .models import Major, Subject, Student, Course


class SubjectInline(admin.StackedInline):
    model = Subject


class MajorAdmin(admin.ModelAdmin):
    inlines = [SubjectInline, ]


# Register your models here. #Model interface
admin.site.register(Major, MajorAdmin)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Course)
