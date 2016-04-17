from common.models import *
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime


@verbose_names
class DynamometryCard(models.Model):
    patient = models.ForeignKey(Patient)
    examiners = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    muscle = models.ForeignKey(to='neurophysiological_study.Muscle')
    duration = models.DurationField()

    max = ShortFloatField(blank=True, null=True)
    max_relative = ShortFloatField(blank=True, null=True)

    average = ShortFloatField(blank=True, null=True)
    average_relative = ShortFloatField(blank=True, null=True)

    surface_area = ShortFloatField(blank=True, null=True)
    relative_surface_area = ShortFloatField(blank=True, null=True)

    standard_deviation = ShortFloatField(blank=True, null=True)

    to_max = ShortFloatField(blank=True, null=True)
    relative_to_max = ShortFloatField(blank=True, null=True)

    to_zero = ShortFloatField(blank=True, null=True)
    relative_to_zero = ShortFloatField(blank=True, null=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'date',)

    def __str__(self):
        return "{0} - {1}".format(self.muscle, self.duration)
