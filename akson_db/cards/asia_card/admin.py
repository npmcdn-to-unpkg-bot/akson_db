from django.contrib import admin
from asia_card.models import *

from common.feature import FeatureCardAdmin
from common.admin import AksonCardAdmin

from django.utils.translation import gettext_lazy as _

class AsiaCardCardAdmin(AksonCardAdmin):
    fieldsets = (
        (_('General'),
            {'fields': (('patient', 'leading_people', 'date'),
            )}),
        (_('Sensory'),
            {'fields': (
                ('sensory_light_touch_R_C2', 'sensory_light_touch_L_C2', 'sensory_pin_prick_R_C2', 'sensory_pin_prick_L_C2'),
                ('sensory_light_touch_R_C3', 'sensory_light_touch_L_C3', 'sensory_pin_prick_R_C3', 'sensory_pin_prick_L_C3'),
                ('sensory_light_touch_R_C4', 'sensory_light_touch_L_C4', 'sensory_pin_prick_R_C4', 'sensory_pin_prick_L_C4'),
                ('sensory_light_touch_R_C5', 'sensory_light_touch_L_C5', 'sensory_pin_prick_R_C5', 'sensory_pin_prick_L_C5'),
                ('sensory_light_touch_R_C6', 'sensory_light_touch_L_C6', 'sensory_pin_prick_R_C6', 'sensory_pin_prick_L_C6'),
                ('sensory_light_touch_R_C7', 'sensory_light_touch_L_C7', 'sensory_pin_prick_R_C7', 'sensory_pin_prick_L_C7'),
                ('sensory_light_touch_R_C8', 'sensory_light_touch_L_C8', 'sensory_pin_prick_R_C8', 'sensory_pin_prick_L_C8'),
                ('sensory_light_touch_R_T1', 'sensory_light_touch_L_T1', 'sensory_pin_prick_R_T1', 'sensory_pin_prick_L_T1'),
                ('sensory_light_touch_R_T2', 'sensory_light_touch_L_T2', 'sensory_pin_prick_R_T2', 'sensory_pin_prick_L_T2'),
                ('sensory_light_touch_R_T3', 'sensory_light_touch_L_T3', 'sensory_pin_prick_R_T3', 'sensory_pin_prick_L_T3'),
                ('sensory_light_touch_R_T4', 'sensory_light_touch_L_T4', 'sensory_pin_prick_R_T4', 'sensory_pin_prick_L_T4'),
                ('sensory_light_touch_R_T5', 'sensory_light_touch_L_T5', 'sensory_pin_prick_R_T5', 'sensory_pin_prick_L_T5'),
                ('sensory_light_touch_R_T6', 'sensory_light_touch_L_T6', 'sensory_pin_prick_R_T6', 'sensory_pin_prick_L_T6'),
                ('sensory_light_touch_R_T7', 'sensory_light_touch_L_T7', 'sensory_pin_prick_R_T7', 'sensory_pin_prick_L_T7'),
                ('sensory_light_touch_R_T8', 'sensory_light_touch_L_T8', 'sensory_pin_prick_R_T8', 'sensory_pin_prick_L_T8'),
                ('sensory_light_touch_R_T9', 'sensory_light_touch_L_T9', 'sensory_pin_prick_R_T9', 'sensory_pin_prick_L_T9'),
                ('sensory_light_touch_R_T10', 'sensory_light_touch_L_T10', 'sensory_pin_prick_R_T10', 'sensory_pin_prick_L_T10'),
                ('sensory_light_touch_R_T11', 'sensory_light_touch_L_T11', 'sensory_pin_prick_R_T11', 'sensory_pin_prick_L_T11'),
                ('sensory_light_touch_R_T12', 'sensory_light_touch_L_T12', 'sensory_pin_prick_R_T12', 'sensory_pin_prick_L_T12'),
                ('sensory_light_touch_R_L1', 'sensory_light_touch_L_L1', 'sensory_pin_prick_R_L1', 'sensory_pin_prick_L_L1'),
                ('sensory_light_touch_R_L2', 'sensory_light_touch_L_L2', 'sensory_pin_prick_R_L2', 'sensory_pin_prick_L_L2'),
                ('sensory_light_touch_R_L3', 'sensory_light_touch_L_L3', 'sensory_pin_prick_R_L3', 'sensory_pin_prick_L_L3'),
                ('sensory_light_touch_R_L4', 'sensory_light_touch_L_L4', 'sensory_pin_prick_R_L4', 'sensory_pin_prick_L_L4'),
                ('sensory_light_touch_R_L5', 'sensory_light_touch_L_L5', 'sensory_pin_prick_R_L5', 'sensory_pin_prick_L_L5'),
                ('sensory_light_touch_R_S1', 'sensory_light_touch_L_S1', 'sensory_pin_prick_R_S1', 'sensory_pin_prick_L_S1'),
                ('sensory_light_touch_R_S2', 'sensory_light_touch_L_S2', 'sensory_pin_prick_R_S2', 'sensory_pin_prick_L_S2'),
                ('sensory_light_touch_R_S3', 'sensory_light_touch_L_S3', 'sensory_pin_prick_R_S3', 'sensory_pin_prick_L_S3'),
                ('sensory_light_touch_R_S45', 'sensory_light_touch_L_S45', 'sensory_pin_prick_R_S45', 'sensory_pin_prick_L_S45'),
                ('deep_anal_pressure',),
            )}),
        (_('Motor'),
            {'fields': (
                ('motor_R_C5', 'motor_L_C5'),
                ('motor_R_C6', 'motor_L_C6'),
                ('motor_R_C7', 'motor_L_C7'),
                ('motor_R_C8', 'motor_L_C8'),
                ('motor_R_T1', 'motor_L_T1'),
                ('motor_R_L2', 'motor_L_L2'),
                ('motor_R_L3', 'motor_L_L3'),
                ('motor_R_L4', 'motor_L_L4'),
                ('motor_R_L5', 'motor_L_L5'),
                ('voluntary_anal_contraction'),
            )}),
        (_('Summary'),
            {'fields': (
                ('complete','ais'),
                )}),
        (_('Additionals'),
            {'fields': (
                ('additional_notes',),
                )}),
            )

admin.site.register(AsiaCard, AsiaCardCardAdmin)

admin.site.register(SensoryIndex, FeatureCardAdmin)
admin.site.register(MotorIndex, FeatureCardAdmin)
