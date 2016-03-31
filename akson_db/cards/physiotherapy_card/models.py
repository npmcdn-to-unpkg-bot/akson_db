from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

from patient.models import Patient
from common.feature import Feature
from common.localization import *
from common.models import *
from django.contrib.auth.models import User

@verbose_names
class PhysiotherapyCard(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    treatment_type = models.ManyToManyField('TreatmentType')
    _('treatment_type')

    area = models.ManyToManyField('Area')
    _('area')

    parameters = DescriptionField()
    _('parameters')

    additional_notes = AdditionalNotesField(blank = True, null = True)
    _('additional_notes')

    class Meta:
        ordering = ('patient', 'date',)
_('physiotherapy_card')
_('physiotherapy_cards')

@verbose_names
class TreatmentType(Feature):
    pass
_('treatment_types')

@verbose_names
class Area(Feature):
    pass
_('areas')
