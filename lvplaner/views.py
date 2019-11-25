from django.shortcuts import render, get_object_or_404
from .models import Major
from django.http import HttpResponse


# Create your views here.


def major_list(request):
    majors = Major.objects.all()
    return render(request, 'lvplaner/major_list.html', {'majors': majors})


def major_detail(request, pk):
    major = get_object_or_404(Major, pk=pk)
    return render(request, 'lvplaner/major_detail.html', {'major': major})
