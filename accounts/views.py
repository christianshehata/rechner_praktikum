from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages

from .forms import UserCreateForm, DeleteUser


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("authentication")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/userlist.html', {'users': users})


def delete_user(request):
    form = DeleteUser
    inventory = User.objects.all()
    if request.method == 'POST':
        item_id = str(request.POST.get('username'))
        item = User.objects.get(username=item_id)
        item.delete()
        messages.success(request, ('User has been deleted!'))
    return render(request, 'accounts/deleteuser.html', {'form': form, 'inventory': inventory})
