from django.shortcuts import render, get_object_or_404
from .models import Major, Subject, Course, Student
from django.http import HttpResponse
from .forms import MajorForm, SubjectForm, CourseForm
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


def delete_major(request):
    form = MajorForm()
    inventory = Major.objects.all()
    if request.method == 'POST':
        item_id = str(request.POST.get('major_name'))
        item = Major.objects.get(major_name=item_id)
        item.delete()
        messages.success(request, ('Major has been deleted!'))
        return HttpResponseRedirect('/')
    return render(request, 'lvplaner/deletemajor.html', {'form': form, 'inventory': inventory})


def createsubject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully added to the database!'))
            return HttpResponseRedirect('/')
    return render(request, 'lvplaner/createsubject.html', {'form': form})


def createcourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Course has been successfully added to the database!'))
            return HttpResponseRedirect('/')
    return render(request, 'lvplaner/createcourse.html', {'form': form})
