from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render_to_response, render, get_object_or_404
from django.urls import reverse

"""
This contains basic user functionality such as
login, logout, registration etc.
Everything to do with the actual AAI is contained
inside the "abschlussarbeiten" folder.
"""


def error_404(request):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


def register(request, next_page_name=None):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if next_page_name is None:
                next_page = '/'
            else:
                next_page = reverse(next_page_name)
            return HttpResponseRedirect(next_page)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout(request):
    messages.info(request, 'Um sich vollständig abzumelden, schließen Sie bitte alle Browser-Fenster!')
    pass
