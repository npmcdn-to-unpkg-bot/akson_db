from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


@verbose_names
class TrackGaitTraining(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    blood_pressure_hr_rest = ShortIntegerField(validators=[MinValueValidator(40), MaxValueValidator(300)])
    blood_pressure_rr_sys = ShortIntegerField(validators=[MinValueValidator(30), MaxValueValidator(250)])
    blood_pressure_rr_dia = ShortIntegerField(validators=[MinValueValidator(20), MaxValueValidator(150)])

    restoration_time = models.TimeField()
    gait_speed = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])  # [m/s]
    gait_time = models.TimeField()  # TODO try datetime.widget = forms.SplitDateTimeWidget(time_format=('%H:%M'))
    gait_time.widget = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    distance = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1000)])  # [m]

    support_type = models.ManyToManyField('SupportType')
    left_orthosis = models.ManyToManyField('gait_reeducation_card.OrthosisType', related_name="LeftOrthosis",
                                           blank=True)
    right_orthosis = models.ManyToManyField('gait_reeducation_card.OrthosisType', related_name="RightOrthosis",
                                            blank=True)

    fixation_location = models.ManyToManyField('FixationLocation')
    load = ShortFloatField(validators=[MinValueValidator(0), MaxValueValidator(30000)])  # [g]
    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class FixationLocation(Feature):
    pass


@verbose_names
class SupportType(Feature):
    pass
