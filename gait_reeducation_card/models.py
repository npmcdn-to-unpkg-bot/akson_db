from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


@verbose_names
class GaitReeducationCard(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)
    tool = models.ManyToManyField('ReeducationTool', blank=True)
    left_orthosis = models.ManyToManyField('OrthosisType', related_name="LeftOrthosis+", blank=True)
    right_orthosis = models.ManyToManyField('OrthosisType', related_name="RightOrthosis+", blank=True)
    distance = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(1000)])  # [m]
    gait_time = models.TimeField()  # TODO try datetime.widget = forms.SplitDateTimeWidget(time_format=('%H:%M'))
    gait_time.widget = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    vertical_load = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(20000)])  # [g]
    horizontal_load = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(30000)])  # [g]

    accented_traits = models.ManyToManyField('AccentedTrait')
    gait_coefficients = models.ManyToManyField('GaitCoefficient')

    akson_gait_index = models.ManyToManyField('AksonGaitIndex')
    assurance_type = models.ForeignKey('AssuranceType')
    displacement_type = models.ForeignKey('DisplacementType')
    additional_notes = AdditionalNotesField(blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.patient, self.date)

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class ReeducationTool(Feature):
    pass


@verbose_names
class OrthosisType(Feature):
    pass


@verbose_names
class AccentedTrait(Feature):
    pass


@verbose_names
class GaitCoefficient(Feature):
    pass


@verbose_names
class AksonGaitIndex(Feature):
    pass


@verbose_names
class AssuranceType(Feature):
    pass


@verbose_names
class DisplacementType(Feature):
    pass
