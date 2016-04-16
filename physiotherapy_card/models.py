from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime


@verbose_names
class PhysiotherapyCard(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)
    treatment_type = models.ManyToManyField('TreatmentType')
    area = models.ManyToManyField('Area')
    parameters = DescriptionField()
    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class TreatmentType(Feature):
    pass


@verbose_names
class Area(Feature):
    pass
