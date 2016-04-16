from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from upper_limb_study.models import *


class UpperLimbStudyCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
            {'fields': (('patient', 'examiners', 'date'),
            )}),
        # part
        ('surface_sense',
            {'fields': (
                ('surface_sense_left_flexor_arm_side', 'surface_sense_right_flexor_arm_side'),
                ('surface_sense_left_rectifier_arm_side', 'surface_sense_right_rectifier_arm_side'),
                ('surface_sense_left_flexor_forearm_side', 'surface_sense_right_flexor_forearm_side'),
                ('surface_sense_left_rectifier_forearm_side', 'surface_sense_right_rectifier_forearm_side'),
                ('surface_sense_left_palmar_hand_side', 'surface_sense_right_palmar_hand_side'),
                ('surface_sense_left_dorsal_hand_side', 'surface_sense_right_dorsal_hand_side'),
                ('surface_sense_left_thumb', 'surface_sense_right_thumb'),
                ('surface_sense_left_index_finger', 'surface_sense_right_index_finger'),
                ('surface_sense_left_finger_3', 'surface_sense_right_finger_3'),
                ('surface_sense_left_ring_finger', 'surface_sense_right_ring_finger'),
                ('surface_sense_left_small_finger', 'surface_sense_right_small_finger'),
                )}),
        ('feeling_limbs_pose',
            {'fields': (
                ('feeling_limbs_pose_left', 'feeling_limbs_pose_right'),
                )}),
        # part
        ('feeling_vibration',
            {'fields': (
                ('feeling_vibration_left_arm', 'feeling_vibration_right_arm'),
                ('feeling_vibration_left_forearm', 'feeling_vibration_right_forearm'),
                ('feeling_vibration_left_hand', 'feeling_vibration_right_hand'),
             )}),
        # part
        ('feeling_pain',
            {'fields': (
                ('feeling_pain_left_arm', 'feeling_pain_right_arm'),
                ('feeling_pain_left_forearm', 'feeling_pain_right_forearm'),
                ('feeling_pain_left_hand', 'feeling_pain_right_hand'),
             )}),
        # part
        ('feeling_cold',
            {'fields': (
                ('feeling_cold_left', 'feeling_cold_right'),
             )}),
        # part
        ('feeling_hot',
            {'fields': (
                ('feeling_hot_left', 'feeling_hot_right'),
             )}),
        # part
        ('feeling_temperature_change',
            {'fields': (
                ('feeling_temperature_change_left', 'feeling_temperature_change_right'),
             )}),
        # part
        ('grip_study',
            {'fields': (
                ('grip_study_left_cylinders_diameter', 'grip_study_right_cylinders_diameter'),
                ('grip_study_left_weight', 'grip_study_right_weight'),
             )}),
        # part
        ('test_reflexes',
            {'fields': (
                ('test_reflexes_left_radial', 'test_reflexes_right_radial'),
                ('test_reflexes_left_cubital', 'test_reflexes_right_cubital'),
                ('test_reflexes_left_bicephalous', 'test_reflexes_right_bicephalous'),
                ('test_reflexes_left_triceps', 'test_reflexes_right_triceps'),
             )}),

        (txt('Additionals'),
            {'fields': (
                ('additional_notes',),
                )}),
            )

    list_display = ('patient', 'date',)

admin.site.register(UpperLimbStudy, UpperLimbStudyCardAdmin)
admin.site.register(SurfaceSense, FeatureCardAdmin)
admin.site.register(FeelingLimbsPose, FeatureCardAdmin)
admin.site.register(FeelingVibration, FeatureCardAdmin)
admin.site.register(FeelingPain, FeatureCardAdmin)
admin.site.register(FeelingTemperature, FeatureCardAdmin)
admin.site.register(TestReflexes, FeatureCardAdmin)
