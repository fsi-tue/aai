import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Thesis
from .tables import ThesisTable
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .filters import ThesisFilter


def index(request):
    messages.info(request, 'Diese Seite befindet sich noch im Aufbau und ist sowieso nur Proof of Concept.')
    return render(request, 'index.html')


def detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, pk=thesis_id)
    return render(request, 'detail.html', {
        'thesis': thesis,
    })


def allentries(request):
    entries = ThesisTable(Thesis.objects.filter(is_active=True))
    return render(request, 'all.html', {
        'allentries': entries
    })


def tags(request):
    tagcloud = Thesis.tags.tag_model.objects.weight()
    return render(request, 'tags.html', {
        'tags': tagcloud
    })


def by_tag(request, slug):
    """
    This view is called when a user highlights a specific tag inside the tagcloud view.
    The database is queried to show all Thesis with this tag, the QuerySet is then
    displayed inside a ThesisTable (see tables.py).
    :param slug:
    :param request: HTTP request object
    :param args: the tag slug to be queried
    :return:
    """
    tag = slug
    thesis_with_tag = ThesisTable(Thesis.objects.filter(tags__slug=tag))
    return render(request, 'by_tag.html', {
        'tag': tag,
        'with_tag': thesis_with_tag
    })


class FilteredThesisView(SingleTableMixin, FilterView):
    table_class = ThesisTable
    model = Thesis
    template_name = 'search.html'

    filterset_class = ThesisFilter
    table = ThesisTable
