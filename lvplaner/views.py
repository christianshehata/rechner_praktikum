from django.shortcuts import render, get_object_or_404
from .models import Major, Subject, Course, Student
from django.http import HttpResponse
from .forms import MajorForm, SubjectForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.


def major_list(request):
    majors = Major.objects.all()
    return render(request, 'lvplaner/major_list.html', {'majors': majors})


def major_detail(request, major_name):
    major = get_object_or_404(Major, pk=major_name)
    return render(request, 'lvplaner/major_detail.html', {'major': major})


def courses(request, major_name, subject_title):
    subject = get_object_or_404(Subject, pk=subject_title)
    return render(request, 'lvplaner/courses.html', {'subject': subject})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'lvplaner/student_list.html', {'students': students})


def createmajor(request):
    form = MajorForm()
    if request.method == 'POST':
        form = MajorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully added to the database!'))
            return HttpResponseRedirect('/')
    return render(request, 'lvplaner/createmajor.html', {'form': form})


def createsubject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully added to the database!'))
            return HttpResponseRedirect('/')
    return render(request, 'lvplaner/createsubject.html', {'form': form})
