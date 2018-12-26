
from django.urls import path
from django_filters.views import FilterView

from .filters import ThesisFilter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.allentries, name='all'),
    path('<int:thesis_id>/', views.detail, name='detail'),
    path('tags', views.tags, name='tags'),
    path('by-tag/<slug:slug>', views.by_tag, name='by_tag'),
    path('search', FilterView.as_view(filterset_class=ThesisFilter, template_name='search.html'), name='search'),
]
