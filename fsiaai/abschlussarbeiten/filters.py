import django_filters
from bootstrap4 import forms

from .models import Thesis, Chair


class ThesisFilter(django_filters.FilterSet):
    chair = django_filters.ModelMultipleChoiceFilter(queryset=Chair.objects.all(),
                                                     widget=forms.CheckboxSelectMultiple)
    type = django_filters.ModelMultipleChoiceFilter(name='type')

    class Meta:
        model = Thesis
        fields = ['chair', 'title', 'start_date', 'type']
