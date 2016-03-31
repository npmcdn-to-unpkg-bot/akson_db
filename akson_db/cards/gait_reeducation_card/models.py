from django.db import models
from django import forms
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from patient.models import Patient
from common.feature import Feature
from common.localization import *
from common.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

@verbose_names
class GaitReeducationCard(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    _('leading_people')
    date = models.DateField(default=datetime.now)
    _('date')
    tool = models.ManyToManyField('ReeducationTool', blank=True)
    _('tool')
    left_orthosis = models.ManyToManyField('OrthosisType', related_name="LeftOrthosis+", blank=True)
    _('left_orthosis')
    right_orthosis = models.ManyToManyField('OrthosisType', related_name="RightOrthosis+", blank=True)
    _('right_orthosis')
    distance = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(1000)]) # [m]
    _('distance')
    gait_time = models.TimeField() # TODO try datetime.widget = forms.SplitDateTimeWidget(time_format=('%H:%M'))
    gait_time.widget = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    _('gait_time')
    vertical_load = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(20000)]) # [g]
    _('vertical_load')
    horizontal_load = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(30000)]) # [g]
    _('horizontal_load')

    accented_traits = models.ManyToManyField('AccentedTrait')
    _('accented_traits')
    gait_coefficients = models.ManyToManyField('GaitCoefficient')
    _('gait_coefficients')

    akson_gait_index = models.ManyToManyField('AksonGaitIndex')
    _('akson_gait_index')

    assurance_type = models.ForeignKey('AssuranceType')
    _('assurance_type')
    displacement_type = models.ForeignKey('DisplacementType')
    _('displacement_type')
    additional_notes = AdditionalNotesField(blank = True, null = True)
    _('additional_notes')

    def __str__(self):
        return "{0} {1}".format(self.patient, self.date)

    class Meta:
        ordering = ('patient', 'date',)

_('gait_reeducation_card')
_('gait_reeducation_cards')

@verbose_names
class ReeducationTool(Feature):
    pass
_('reeducation_tool')
_('reeducation_tools')

@verbose_names
class OrthosisType(Feature):
    pass
_('orthosis_type')
_('orthosis_types')

@verbose_names
class AccentedTrait(Feature):
    pass
_('accented_trait')

@verbose_names
class GaitCoefficient(Feature):
    pass
_('gait_coefficient')

@verbose_names
class AksonGaitIndex(Feature):
    pass
_('akson_gait_indexs')

@verbose_names
class AssuranceType(Feature):
    pass
_('assurance_types')

@verbose_names
class DisplacementType(Feature):
    pass
_('displacement_types')
