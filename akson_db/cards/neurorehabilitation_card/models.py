from django.db import models
from django import forms
from datetime import datetime
from django.utils.translation import gettext_lazy as _

from patient.models import Patient
from common.feature import Feature
from common.localization import *
from common.models import *
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

@verbose_names
class NeurorehabilitationCard(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    excercise_signature = models.ForeignKey('ExcerciseSignature')
    _('excercise_signature')

    load = ShortFloatField(validators=[MinValueValidator(-40000), MaxValueValidator(40000)]) # [g]
    _('load')
    repetitions = ShortIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    _('repetitions')
    sets = ShortIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    _('sets')

    starting_position = models.ForeignKey('StartingPosition')
    _('starting_position')
    nature_of_load = models.ManyToManyField('NatureOfLoad', blank=True)
    _('nature_of_load')
    motion_range = models.ManyToManyField('MotionRange', blank=True)
    _('motion_range')

    time = models.TimeField(blank=True, null=True) # TODO try datetime.widget = forms.SplitDateTimeWidget(time_format=('%H:%M'))
    time.widget = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    frequency = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(40)], blank=True, null=True) # [Hz]
    _('frequency')

    additional_notes = AdditionalNotesField(blank = True, null = True)
    _('additional_notes')

    class Meta:
        ordering = ('patient', 'date',)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.excercise_signature, self.load, self.repetitions)
_('neurorehabilitation_card')
_('neurorehabilitation_cards')

@verbose_names
class ExcerciseSignature(Feature):
    pass
_('excercise_signatures')

@verbose_names
class StartingPosition(Feature):
    pass
_('starting_positions')

@verbose_names
class NatureOfLoad(Feature):
    pass
_('nature_of_loads')

@verbose_names
class MotionRange(Feature):
    pass
_('motion_ranges')

