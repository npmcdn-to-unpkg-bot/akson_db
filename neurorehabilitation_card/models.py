from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


@verbose_names
class NeurorehabilitationCard(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    excercise_signature = models.ForeignKey('ExcerciseSignature')
    load = ShortFloatField(validators=[MinValueValidator(-40000), MaxValueValidator(40000)])  # [g]
    repetitions = ShortIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
    sets = ShortIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    starting_position = models.ForeignKey('StartingPosition')
    nature_of_load = models.ManyToManyField('NatureOfLoad', blank=True)
    motion_range = models.ManyToManyField('MotionRange', blank=True)

    # TODO try datetime.widget = forms.SplitDateTimeWidget(time_format=('%H:%M'))
    time = models.TimeField(blank=True, null=True)
    time.widget = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    frequency = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(40)], blank=True, null=True)  # [Hz]

    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'date',)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.excercise_signature, self.load, self.repetitions)


@verbose_names
class ExcerciseSignature(Feature):
    pass


@verbose_names
class StartingPosition(Feature):
    pass


@verbose_names
class NatureOfLoad(Feature):
    pass


@verbose_names
class MotionRange(Feature):
    pass
