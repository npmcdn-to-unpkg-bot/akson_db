from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime


@verbose_names
class TimeSpread(models.Model):
    patient = models.ForeignKey(Patient)
    leading_doctors = models.ManyToManyField(User)

    # time spreads
    begin = models.DateField(default=datetime.now)
    end = models.DateField(blank=True, null=True)

    # coefficients
    asia = models.ManyToManyField('ASIA', blank=True)
    icd10 = DescriptionField(blank=True, null=True)
    ashworth = models.ManyToManyField('Ashworth', blank=True)

    # diagnosis
    diagnosis = DescriptionField(blank=True, null=True)
    contraindicators = DescriptionField(blank=True, null=True)
    levels_of_injury = models.ManyToManyField('LevelOfInjury')
    injury_unit = models.TextField()

    # treatment
    date_of_agreement = models.DateField(blank=True, null=True)
    rehabilitation_at_home = models.BooleanField(default=False)

    def __str__(self):
        return "{0} {1} | {2} - {3}".format(self.patient.first_name, self.patient.last_name, self.begin, self.end)

    class Meta:
        ordering = ('patient', 'begin',)


@verbose_names
class ASIA(Feature):
    pass


@verbose_names
class ICD10(Feature):
    pass


@verbose_names
class Ashworth(Feature):
    pass


@verbose_names
class LevelOfInjury(Feature):
    pass
