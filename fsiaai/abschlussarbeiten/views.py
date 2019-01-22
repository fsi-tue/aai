import os

from django.core.files.storage import FileSystemStorage
from django_tables2 import RequestConfig
from tagulous.utils import render_tags
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Thesis
from .tables import ThesisTable
from django.contrib.auth.decorators import login_required


def index(request):
    messages.info(request, 'Diese Seite befindet sich noch im Aufbau und ist sowieso nur Proof of Concept.')
    return render(request, 'index.html')

@login_required
def detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, pk=thesis_id)
    return render(request, 'detail.html', {
        'thesis': thesis,
    })

@login_required
def allentries(request):
    entries = ThesisTable(Thesis.objects.filter(is_active=True))
    RequestConfig(request).configure(entries)  # for sorting
    return render(request, 'all.html', {
        'allentries': entries
    })

@login_required
def tags(request):
    tagcloud = Thesis.tags.tag_model.objects.weight()
    return render(request, 'tags.html', {
        'tags': tagcloud
    })

@login_required
def by_tag(request, slug):
    """
    This view is called when a user highlights a specific tag inside the tagcloud view.
    The database is queried to show all Thesis with this tag, the QuerySet is then
    displayed inside a ThesisTable (see tables.py).
    :param slug: the tag slug to be queried
    :param request: HTTP request object
    :return:
    """
    tag = slug
    thesis_with_tag = ThesisTable(Thesis.objects.filter(tags__slug=tag))
    RequestConfig(request).configure(thesis_with_tag)  # for sorting
    return render(request, 'by_tag.html', {
        'tag': tag,
        'with_tag': thesis_with_tag
    })
