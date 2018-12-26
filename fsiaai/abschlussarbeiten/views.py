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
