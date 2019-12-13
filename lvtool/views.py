from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from .forms import SuggestionForm
from django.views.generic import View


def hello_world(request):
    return render(request, 'authentication.html')


def home(request):
    return render(request, 'home.html')


# Feedback
def suggestion_view(request):
    form = SuggestionForm()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            print('Form ✔️')
            send_mail(
                'Suggestion form {}'.format(form.cleaned_data['name']),
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['c.shehata112@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS, 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello World though!')
