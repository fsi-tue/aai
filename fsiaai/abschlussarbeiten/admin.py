from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.forms import FileField, FileInput

from .models import Thesis, Chair, AAIUser

# admin.site.register(Thesis)
admin.site.register(Chair)


@admin.register(Thesis)
class ThesisAdmin(ModelAdmin):
    list_display = ('title', 'type', 'is_active', 'chair')

    @staticmethod
    def has_change_permission(request, obj=None):
        if ThesisAdmin.can_make_changes(obj, request):
            return True
        else:
            return False

    @staticmethod
    def has_delete_permission(request, obj=None):
        if ThesisAdmin.can_make_changes(obj, request):
            return True
        else:
            return False

    @staticmethod
    def can_make_changes(thesis, request):
        """
        If a user is able to make changes to a model entry, they recieve the usual ModelForm.
        If not, they get a read-only view of the entry.
        :param thesis:
        :param request:
        :return:
        """
        return thesis is None \
               or request.user.chair_id == thesis.chair.id \
               or request.user.id == thesis.user.id \
               or request.user.is_superuser \
               or request.user.has_group('moderatoren')

    # def has_add_permission(self, request,obj=None):
    #     return True
    """
    def get_queryset(self, request):
        queryset = super(ThesisAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.has_group('moderatoren'):
            return queryset
        return queryset.filter(user=request.user)
    """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        We overload the formfield_for_foreignkey field to restrict users that are not superuser or moderators from:
        * choosing other persons than themselves as uploaders of a Thesis
        * choosing other chairs than their own as the chair providing a Thesi
        :param db_field: referring to the Thesis model fields 'user' and 'chair'
        :param request: contains the user that is logged in at the moment
        :param kwargs: modified QuerySets are passed to the FormField inside the django admin via kwargs.
        :return:
        """
        if not request.user.is_superuser or request.user.has_group('moderatoren'):
            if db_field.name == 'user':
                qs = AAIUser.objects.filter(username=request.user.username)
                kwargs['queryset'] = qs
                kwargs['initial'] = qs
            if db_field.name == 'chair':
                qs = Chair.objects.filter(employed_at=request.user)
                kwargs['queryset'] = qs
                kwargs['initial'] = qs
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class MyUserChangeForm(UserChangeForm):
    """
    Used to override the regular Django Admin form for changing user details.
    This enables us (via MyUserAdmin below) to put in extra fields etc.,
    """

    class Meta(UserChangeForm.Meta):
        model = AAIUser


class MyUserAdmin(UserAdmin):
    """
    This overrides the typical UserAdminForm to display additional information.
    In this case, it is to select the relationship to the Chair model.
    """
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('chair',)}),
    )
    list_display = ('username', 'first_name', 'last_name', 'email', 'chair')


admin.site.register(AAIUser, MyUserAdmin)
