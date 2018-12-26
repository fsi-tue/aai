import django_tables2 as tables
from django.http import request
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Chair, Thesis
from django_tables2.utils import A

"""
Here, we declare tables that operate directly on top of our model,
displaying various columns of the Thesis model. The columns to be displayed are dictated by the Meta class 
of each table, the QuerySet to be used is selected in the view itself.
The tables are then renderd in the template via the {% render_table table_name %} command.
"""


class ThesisTable(tables.Table):
    """
    Displays a table for all the thesis that are currently available.
    (filter statement is in the corresponding view, since Django won't let me filter otherwise)
    """
    class Meta:
        model = Thesis
        attrs = {'class': 'table table-responsive thesis'}  # renders css class
        exclude = ['thesis_id', 'contact', 'is_active', 'pdf']

    link = tables.LinkColumn('detail', args=[A('pk')], orderable=False, empty_values=())

    def render_link(self, record):
        return mark_safe('<a href=' + reverse('detail', args=[record.pk]) + '>Details</a>')

