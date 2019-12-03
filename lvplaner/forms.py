from django import forms
from django.forms import ModelForm

from lvplaner.models import Major, Subject, Course


class MajorForm(ModelForm):
    class Meta:
        model = Major
        fields = "__all__"
        name = forms.CharField()


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        name = forms.CharField()


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        name = forms.CharField()
