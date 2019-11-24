from django.shortcuts import render
from .models import Major
from django.http import HttpResponse


# Create your views here.

#
# def major_list(request):
#     majors = Major.objects.all()
#     return render(request, 'lvplaner/major_list.html', {'majors': majors})

def major_list(request):
    majors = Major.objects.all()
    return render(request, 'lvplaner/major_list.html', {'majors': majors})

