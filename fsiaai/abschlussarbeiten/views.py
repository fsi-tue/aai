from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Thesis
from .tables import ThesisTable
from django.forms.utils import flatatt


def index(request):
    return render(request, 'index.html')


def detail(request, thesis_id):
    response = "You're looking at the detail page of thesis %s."
    return HttpResponse(response % thesis_id)


def allentries(request):
    entries = ThesisTable(Thesis.objects.filter(is_active=True))
    return render(request, 'all.html', {
        'allentries': entries
    })
