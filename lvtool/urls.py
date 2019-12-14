"""lvtool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('lvplaner/', include('lvplaner.urls')),
    path('accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('hello/', views.HelloWorldView.as_view(), name='hello'),
    path('suggest/', views.suggestion_view, name='suggestion'),
    path('', views.hello_world, name='authentication'),
    path('home/', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
