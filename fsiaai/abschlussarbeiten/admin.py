from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import Thesis, Chair, AAIUser

# admin.site.register(Thesis)
admin.site.register(Chair)


@admin.register(Thesis)
class ThesisAdmin(ModelAdmin):
    """
    ForeignKey field.
    If user is "mitarbeiter", only show Thesis of their own chair and enable them to only choose their own chair when creating one.
    Maybe log which user created model entry with https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    """

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
        return thesis is None \
               or request.user.chair_id == thesis.chair.id \
               or request.user.id == thesis.user.id \
               or request.user.is_superuser

    # def has_add_permission(self, request,obj=None):
    #     return True

    pass


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
