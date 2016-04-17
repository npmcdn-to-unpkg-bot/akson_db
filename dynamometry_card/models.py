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

    max_dynamometer = ShortFloatField()
    max_relative_dynamometer = ShortFloatField()

    average_dynamometer = ShortFloatField()
    average_relative_dynamometer = ShortFloatField()

    dynamometer_surface_area = ShortFloatField()
    dynamometer_relative_surface_area = ShortFloatField()

    dynamometer_standard_deviation = ShortFloatField()

    dynamometer_to_max = ShortFloatField()
    dynamometer_relative_to_max = ShortFloatField()

    dynamometer_to_zero = ShortFloatField()
    dynamometer_relative_to_zero = ShortFloatField()

    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'date',)

    def __str__(self):
        return "{0} - {1}".format(self.muscle, self.duration)
