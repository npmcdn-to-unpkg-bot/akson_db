from common.models import *
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
    MVIC = ShortFloatField()
    relative_MVIC = ShortFloatField()

    max_EMG = ShortFloatField()
    max_relative_EMG = ShortFloatField()

    average_EMG = ShortFloatField()
    average_relative_EMG = ShortFloatField()

    EMG_surface_area = ShortFloatField()
    EMG_relative_surface_area = ShortFloatField()

    EMG_standard_deviation = ShortFloatField()

    WNM = ShortFloatField()

    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'date',)

    def __str__(self):
        return "{0} - {1}".format(self.mass, self.WNM)
