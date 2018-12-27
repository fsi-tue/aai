import tagulous.models
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from tagulous.utils import parse_tags


class Chair(models.Model):
    name = models.CharField('Lehrstuhl-name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lehrstuhl"
        verbose_name_plural = "Lehrstühle"


class Thesis(models.Model):
    """
    This class defines the field that a thesis can have.
    The following fields are optional: additional, pdf
    A thesis can be promoted for either BSc, MSc, BEd, MEd, or as being part of a project.
    Each thesis is referenced with the chair that is providing it via a ForeignKey field.
    """
    THESIS_CHOICES = (
        ('BSC', 'Bachelor of Science'),
        ('MSC', 'Master of Science'),
        ('BED', 'Bachelor of Education'),
        ('MED', 'Master of Education'),
        ('PRO', 'Forschungsprojekt'),
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

    start_date = models.DateField('frühester Beginn',
                                  blank=False,
                                  default=timezone.now)

    is_active = models.BooleanField('aktiv',
                                    default=True)

    pdf = models.FileField('PDF mit Ausschreibung',
                           blank=True)

    type = models.CharField('Art der Arbeit',
                            max_length=3,
                            choices=THESIS_CHOICES,
                            blank=False)

    tags = tagulous.models.TagField(get_absolute_url=lambda tag: reverse(
            'by_tag',
            args=parse_tags(tag.slug)))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%i/" % self.id

    class Meta:
        verbose_name = "Abschlussarbeit"
        verbose_name_plural = "Abschlussarbeiten"

