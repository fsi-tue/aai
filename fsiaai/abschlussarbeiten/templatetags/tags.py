from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Queries the user that's logged in against user groups in our DB
    in order to display certain items in views.
    from: http://stackoverflow.com/a/34572799
    """
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()

