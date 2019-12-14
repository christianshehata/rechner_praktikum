from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('users/', views.user_list, name='users'),
    path('deleteusers/', views.delete_user, name='deleteusers'),
]