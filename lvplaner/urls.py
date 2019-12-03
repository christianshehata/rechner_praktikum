from django.conf.urls import url
from . import views
from django.urls import path

# you can use path or url

urlpatterns = [
    url(r'^$', views.major_list, name='list'),
    path('createmajor/', views.createmajor, name='createmajor'),
    path('createsubject/', views.createsubject, name='createsubject'),
    path('createcourse/', views.createcourse, name='createcourse'),
    path('deletemajor/', views.delete_major, name='deletemajor'),
    path('students', views.student_list, name='students'),
    url(r'^(?P<major_name>[-\w\d]+)/$', views.major_detail, name='details'),
    url(r'^(?P<major_name>[-\w\d]+)/(?P<subject_title>[-\w\d\s]+)/$', views.courses, name='courses'),
]
