from django.contrib import auth
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Erstellt die für die Funktion benötigten Nutzergruppen.'

    def handle(self, *args, **options):
        Group.objects.update_or_create(name='mitarbeiter')
        Group.objects.update_or_create(name='moderatoren')
        Group.objects.update_or_create(name='studenten')

        mitarbeiter = Group.objects.get(name='mitarbeiter')
        moderatoren = Group.objects.get(name='moderatoren')
        studenten = Group.objects.get(name='studenten')

        perms_mitarbeiter = [
            # Permission.objects.get(codename='is_staff'),
            Permission.objects.get(codename='add_thesis'),
            Permission.objects.get(codename='delete_thesis'),
            Permission.objects.get(codename='change_thesis'),
        ]
        perms_moderatoren = [
            # Permission.objects.get(codename='is_staff'),
            Permission.objects.get(codename='add_aaisuser'),
            Permission.objects.get(codename='change_aaiuser'),
            Permission.objects.get(codename='delete_aaiuser'),
            Permission.objects.get(codename='add_thesis'),
            Permission.objects.get(codename='delete_thesis'),
            Permission.objects.get(codename='change_thesis'),
            Permission.objects.get(codename='add_chair'),
            Permission.objects.get(codename='delete_chair'),
            Permission.objects.get(codename='change_chair'),
        ]
        perms_studenten = [
        ]

        mitarbeiter.permissions.set(perms_mitarbeiter)
        moderatoren.permissions.set(perms_moderatoren)
        studenten.permissions.set(perms_studenten)

        self.stdout.write('Nutzergruppen mit Berechtigungen wurden erstellt.')
