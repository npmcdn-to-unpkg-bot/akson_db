from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime


@verbose_names
class NeurophysiologicalStudy(models.Model):
    patient = models.ForeignKey(Patient)
    examiners = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    mass = ShortFloatField()
    muscle = models.ForeignKey('Muscle')

    MVIC = ShortFloatField(blank=True, null=True)
    relative_MVIC = ShortFloatField(blank=True, null=True)

    max_EMG = ShortFloatField(blank=True, null=True)
    max_relative_EMG = ShortFloatField(blank=True, null=True)

    average_EMG = ShortFloatField(blank=True, null=True)
    average_relative_EMG = ShortFloatField(blank=True, null=True)

    EMG_surface_area = ShortFloatField(blank=True, null=True)
    EMG_relative_surface_area = ShortFloatField(blank=True, null=True)

    EMG_standard_deviation = ShortFloatField(blank=True, null=True)

    WNM = ShortFloatField(blank=True, null=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'date',)

    def __str__(self):
        return "{0} - {1}".format(self.mass, self.WNM)


@verbose_names
class Muscle(Feature):
    pass
