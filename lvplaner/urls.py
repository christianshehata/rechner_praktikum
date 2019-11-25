from django.conf.urls import url
from . import views
from django.urls import path


# you can use path or url

urlpatterns = [
    path(r'(?P<pk>\d+)/$', views.major_detail),
    url(r'^$', views.major_list),


]