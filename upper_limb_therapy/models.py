from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime


@verbose_names
class UpperLimbTherapy(models.Model):
    patient = models.ForeignKey(Patient)
    therapist = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    therapy_detailed_target = models.ManyToManyField('TherapyDetailedTarget')

    left_area = models.ManyToManyField('TherapyArea', related_name="LeftTherapyArea", blank=True)
    right_area = models.ManyToManyField('TherapyArea', related_name="RightTherapyArea", blank=True)

    used_methods_techniques = models.ManyToManyField('TherapyUsedMethodsTechniques')

    additional_notes = AdditionalNotesField(blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.patient.first_name, self.patient.last_name, self.date)

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class TherapyDetailedTarget(Feature):
    pass


@verbose_names
class TherapyArea(Feature):
    pass


@verbose_names
class TherapyUsedMethodsTechniques(Feature):
    pass
