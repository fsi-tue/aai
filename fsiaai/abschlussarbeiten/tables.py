import django_tables2 as tables
from django.http import request
from django.urls import reverse
from django.utils.safestring import mark_safe


from .models import Chair, Thesis
from .filters import ThesisFilter
from django_tables2.utils import A

"""
Here, we declare tables that operate directly on top of our model,
displaying various columns of the Thesis model. The columns to be displayed are dictated by the Meta class 
of each table, the QuerySet to be used is selected in the view itself.
The tables are then renderd in the template via the {% render_table table_name %} command.
"""


class TruncatedTextColumn(tables.Column):
    """
    This column truncates the output of a text column if it is longer than 202 characters.
    If so, the first 199 characters are displayed, followed by an elipsis (...).
    """
    def render(self, value):
        if len(value) > 202:
            return value[0:199] + '...'
        return str(value)


class ThesisTable(tables.Table):
    """
    Displays a table for all the thesis that are currently available.
    (filter statement is in the corresponding view, since Django won't let me filter otherwise)
    """
    class Meta:
        model = Thesis
        attrs = {'class': 'table table-responsive thesis'}  # renders css class
        exclude = ['id', 'contact', 'additional', 'is_active', 'pdf']

    title = tables.Column(linkify=True)  # works since get_absolute_url() is defined for the Thesis model
    description = TruncatedTextColumn(accessor=A('description'))

