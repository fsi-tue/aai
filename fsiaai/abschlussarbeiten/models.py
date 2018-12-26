from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
from django.utils import timezone


class Chair(models.Model):
    name = models.CharField('Lehrstuhl-name', max_length=100)


class Thesis(models.Model):
    """
    This class defines the field that a thesis can have.
    The following fields are optional: additional, pdf
    A thesis can be promoted for either BSc, MSc, BEd, MEd, or as being part of a project.
    Each thesis is referenced with the chair that is providing it via a ForeignKey field.
    """
    BSC = 'B.Sc.'
    MSC = 'M.Sc.'
    BED = 'B.Ed.'
    MED = 'M.Ed.'
    PRO = 'Project'
    THESIS_CHOICES = (
        (BSC, 'Bachelor of Science'),
        (MSC, 'Master of Science'),
        (BED, 'Bachelor of Education'),
        (MED, 'Master of Education'),
        (PRO, 'Forschungsprojekt'),
    )

    title = models.CharField('Titel der Arbeit',
                             blank=False,
                             max_length=200)

    description = models.TextField('Beschreibung',
                                   blank=False)

    date_added = models.DateTimeField('Erstellungsdatum',
                                      default=timezone.now,
                                      editable=False)

    additional = models.TextField('weitere Beschreibung',
                                  blank=True,
                                  max_length=1000)

    contact = models.EmailField('E-Mail der Kontaktperson:',
                                blank=False)

    chair = models.ForeignKey(Chair, on_delete=models.DO_NOTHING,
                              related_name="provided_by",
                              verbose_name='angeboten durch Lehrstuhl')

    start_date = models.DateTimeField('frühester Beginn',
                                      blank=False,
                                      default=timezone.now)

    is_active = models.BooleanField('aktiv',
                                    default=True)

    pdf = models.FileField('PDF mit Ausschreibung',
                           upload_to='uploads/',
                           blank=True)

    type = models.CharField(max_length=3,
                            choices=THESIS_CHOICES,
                            blank=False)

