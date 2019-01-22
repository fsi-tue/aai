import tagulous.models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import FileExtensionValidator
from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from tagulous.utils import parse_tags


class Chair(models.Model):
    name = models.CharField('Lehrstuhl-Name', max_length=100, blank=False)
    head = models.CharField('Leitung', max_length=50, default='')

    def __str__(self):
        return self.name+" ("+self.head+")"

    class Meta:
        verbose_name = "Lehrstuhl"
        verbose_name_plural = "Lehrstühle"


class AAIUser(AbstractUser):
    """
        A custom user object is needed to process the group attributes
        that we receive through SAML2/Shibboleth.
        """
    chair = models.OneToOneField(Chair,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 related_name='employed_at',
                                 verbose_name="Angestellt bei Lehrstuhl")

    pass

    def process_groups(self, groups):
        """
        This is called to process the 'eduPersonAffiliation' attribute
        of the user authenticating with SAML.
        If eduPersonAffiliation of a user contains 'employee', we add them
        to our internal 'dozenten' group. Everything else is handed over to Django.

        :param groups: list of groups the user belongs to
        """
        if 'employee' in groups:
            dozenten = Group.objects.get(name='dozenten')
            dozenten.user_set.add(self)
            self.is_staff = True  # backend login
        pass

    def has_group(self, group):
        """
        handy way to check if our current user is member of a certain group.
        """
        return self.groups.filter(name__in=[group]).exists()


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
        ('ETC', 'nach Absprache')
    )

    COURSE_CHOICES = (
        ('INFO', 'Informatik'),
        ('BIOINF', 'Bioinformatik'),
        ('MEINF', 'Medieninformatik'),
        ('MDZINF', 'Medizininformatik'),
        ('KOGNI', 'Kognitionswissenschaft'),

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

    chair = models.ForeignKey(Chair, on_delete=models.CASCADE,
                              related_name="provided_by",
                              verbose_name='angeboten durch Lehrstuhl')

    start_date = models.DateField('frühester Beginn',
                                  blank=False,
                                  default=timezone.now)

    is_active = models.BooleanField('aktiv',
                                    default=True)

    pdf = models.FileField('PDF mit Ausschreibung',
                           validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                           blank=True)

    type = MultiSelectField('Art der Arbeit',
                            choices=THESIS_CHOICES,
                            default=THESIS_CHOICES[-1][0],  # ETC
                            blank=False)

    courses = MultiSelectField('geeignete Studiengänge',
                               choices=COURSE_CHOICES,
                               default=COURSE_CHOICES[0][0],  # INFO
                               blank=False)

    tags = tagulous.models.TagField(get_absolute_url=lambda tag: reverse(
            'by_tag',
            args=parse_tags(tag.slug)))

    user = models.ForeignKey(AAIUser, null=True,
                             on_delete=models.DO_NOTHING,
                             related_name="uploaded_by",
                             verbose_name="hochgeladen von")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%i/" % self.id

    class Meta:
        verbose_name = "Abschlussarbeit"
        verbose_name_plural = "Abschlussarbeiten"
