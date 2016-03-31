from django.db import models
from django import forms
from datetime import datetime
from django.utils.translation import gettext_lazy as _

from patient.models import Patient
from common.feature import Feature
from common.localization import *
from common.models import *

@verbose_names
class AsiaCard(models.Model):
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField('person.Person')
    date = models.DateField(default=datetime.now)
    _('date')

    sensory_light_touch_R_C2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_C2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_C2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_C2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_C3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_C3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_C3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_C3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_C4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_C4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_C4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_C4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_C5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_C5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_C5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_C5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_C6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_C6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_C6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_C6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_C7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_C7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_C7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_C7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_C8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_C8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_C8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_C8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T6 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T7 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T8 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T9 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T9 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T9 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T9 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T10 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T10 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T10 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T10 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T11 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T11 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T11 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T11 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_T12 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_T12 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_T12 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_T12 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_L1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_L1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_L1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_L1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_L2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_L2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_L2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_L2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_L3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_L3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_L3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_L3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_L4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_L4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_L4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_L4 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_L5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_L5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_L5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_L5 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_S1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_S1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_S1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_S1 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_S2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_S2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_S2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_S2 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_S3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_S3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_S3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_S3 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    sensory_light_touch_R_S45 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_light_touch_L_S45 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_R_S45 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);
    sensory_pin_prick_L_S45 = models.ForeignKey('SensoryIndex', related_name='+', blank = True, null = True);

    motor_R_C5 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_C5 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_C6 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_C6 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_C7 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_C7 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_C8 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_C8 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_T1 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_T1 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_L2 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_L2 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_L3 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_L3 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_L4 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_L4 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_L5 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_L5 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    motor_R_S1 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);
    motor_L_S1 = models.ForeignKey('MotorIndex', related_name='+', blank = True, null = True);

    deep_anal_pressure = models.BooleanField(default=False)
    _('deep_anal_pressure')

    voluntary_anal_contraction = models.BooleanField(default=False)
    _('voluntary_anal_contraction')

    complete = models.BooleanField(default=False)
    _('complete')

    AIS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    ais = models.CharField(max_length=1, choices=AIS)
    _('ais')

    additional_notes = AdditionalNotesField(blank = True, null = True)
    _('additional_notes')

    class Meta:
        ordering = ['date']
_('asia_card')
_('asia_cards')

@verbose_names
class SensoryIndex(Feature):
    pass
_('sensory_index')
_('sensory_indexes')

@verbose_names
class MotorIndex(Feature):
    pass
_('motor_index')
_('motor_indexes')

