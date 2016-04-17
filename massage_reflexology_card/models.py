from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime


@verbose_names
class MassageReflexologyCard(models.Model):
    patient = models.ForeignKey(Patient)
    therapist = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    massage_reflexology_treatment = models.ManyToManyField('MassageReflexologyTreatment')
    massage_reflexology_area = models.ManyToManyField('MassageReflexologyArea')

    additional_notes = AdditionalNotesField(blank=True, null=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.patient.first_name, self.patient.last_name, self.date)

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class MassageReflexologyTreatment(Feature):
    pass


@verbose_names
class MassageReflexologyArea(Feature):
    pass
