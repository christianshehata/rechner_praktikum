from django.conf.urls import url
from . import views
from django.urls import path

# you can use path or url

urlpatterns = [
    url(r'^$', views.major_list),
    url(r'^(?P<major_name>[-\w\d]+)/$', views.major_detail, name='details'),

]
