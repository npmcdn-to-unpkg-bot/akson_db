from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


@verbose_names
class UpperLimbStudy(models.Model):
    patient = models.ForeignKey(Patient)
    examiners = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    surface_sense_left_flexor_arm_side = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftFlexorArm",
                                                           blank=True, null=True)
    surface_sense_right_flexor_arm_side = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightFlexorArm",
                                                            blank=True, null=True)

    surface_sense_left_rectifier_arm_side = models.ForeignKey('SurfaceSense',
                                                              related_name="SurfaceSenseLeftRectifierArm", blank=True,
                                                              null=True)
    surface_sense_right_rectifier_arm_side = models.ForeignKey('SurfaceSense',
                                                               related_name="SurfaceSenseRightRectifierArm", blank=True,
                                                               null=True)

    surface_sense_left_flexor_forearm_side = models.ForeignKey('SurfaceSense',
                                                               related_name="SurfaceSenseLeftFlexorForearm", blank=True,
                                                               null=True)
    surface_sense_right_flexor_forearm_side = models.ForeignKey('SurfaceSense',
                                                                related_name="SurfaceSenseRightFlexorForearm",
                                                                blank=True, null=True)

    surface_sense_left_rectifier_forearm_side = models.ForeignKey('SurfaceSense',
                                                                  related_name="SurfaceSenseLeftRectifierForearm",
                                                                  blank=True, null=True)
    surface_sense_right_rectifier_forearm_side = models.ForeignKey('SurfaceSense',
                                                                   related_name="SurfaceSenseRightRectifierForearm",
                                                                   blank=True, null=True)

    surface_sense_left_palmar_hand_side = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftPalmarHand",
                                                            blank=True, null=True)
    surface_sense_right_palmar_hand_side = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightPalmarHand",
                                                             blank=True, null=True)

    surface_sense_left_dorsal_hand_side = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftDorsalHand",
                                                            blank=True, null=True)
    surface_sense_right_dorsal_hand_side = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightDorsalHand",
                                                             blank=True, null=True)

    surface_sense_left_thumb = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftThumb", blank=True,
                                                 null=True)
    surface_sense_right_thumb = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightThumb", blank=True,
                                                  null=True)

    surface_sense_left_index_finger = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftIndexFinger",
                                                        blank=True, null=True)
    surface_sense_right_index_finger = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightIndexFinger",
                                                         blank=True, null=True)

    surface_sense_left_finger_3 = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftFinger3", blank=True,
                                                    null=True)
    surface_sense_right_finger_3 = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightFinger3",
                                                     blank=True, null=True)

    surface_sense_left_ring_finger = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftRingFinger",
                                                       blank=True, null=True)
    surface_sense_right_ring_finger = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightRingFinger",
                                                        blank=True, null=True)

    surface_sense_left_small_finger = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseLeftSmallFinger",
                                                        blank=True, null=True)
    surface_sense_right_small_finger = models.ForeignKey('SurfaceSense', related_name="SurfaceSenseRightSmallFinger",
                                                         blank=True, null=True)

    feeling_limbs_pose_left = models.ForeignKey('FeelingLimbsPose', related_name="FeelingLimbsPoseLeft", blank=True,
                                                null=True)
    feeling_limbs_pose_right = models.ForeignKey('FeelingLimbsPose', related_name="FeelingLimbsPoseRight", blank=True,
                                                 null=True)

    feeling_vibration_left_arm = models.ForeignKey('FeelingVibration', related_name='FeelingVibrationLeftArm',
                                                   blank=True, null=True)
    feeling_vibration_right_arm = models.ForeignKey('FeelingVibration', related_name='FeelingVibrationRightArm',
                                                    blank=True, null=True)

    feeling_vibration_left_forearm = models.ForeignKey('FeelingVibration', related_name='FeelingVibrationLeftForearm',
                                                       blank=True, null=True)
    feeling_vibration_right_forearm = models.ForeignKey('FeelingVibration', related_name='FeelingVibrationRightForearm',
                                                        blank=True, null=True)

    feeling_vibration_left_hand = models.ForeignKey('FeelingVibration', related_name='FeelingVibrationLeftHand',
                                                    blank=True, null=True)
    feeling_vibration_right_hand = models.ForeignKey('FeelingVibration', related_name='FeelingVibrationRightHand',
                                                     blank=True, null=True)

    feeling_pain_left_arm = models.ForeignKey('FeelingPain', related_name='FeelingPainLeftArm', blank=True, null=True)
    feeling_pain_right_arm = models.ForeignKey('FeelingPain', related_name='FeelingPainRightArm', blank=True, null=True)

    feeling_pain_left_forearm = models.ForeignKey('FeelingPain', related_name='FeelingPainLeftForearm', blank=True,
                                                  null=True)
    feeling_pain_right_forearm = models.ForeignKey('FeelingPain', related_name='FeelingPainRightForearm', blank=True,
                                                   null=True)

    feeling_pain_left_hand = models.ForeignKey('FeelingPain', related_name='FeelingPainLeftHand', blank=True, null=True)
    feeling_pain_right_hand = models.ForeignKey('FeelingPain', related_name='FeelingPainRightHand', blank=True,
                                                null=True)

    feeling_cold_left = models.ForeignKey('FeelingTemperature', related_name='FeelingTemperatureLeftCold', blank=True,
                                          null=True)
    feeling_cold_right = models.ForeignKey('FeelingTemperature', related_name='FeelingTemperatureRightCold', blank=True,
                                           null=True)

    feeling_hot_left = models.ForeignKey('FeelingTemperature', related_name='FeelingTemperatureLeftHot', blank=True,
                                         null=True)
    feeling_hot_right = models.ForeignKey('FeelingTemperature', related_name='FeelingTemperatureRightHot', blank=True,
                                          null=True)

    feeling_temperature_change_left = models.ForeignKey('FeelingTemperature',
                                                        related_name='FeelingTemperatureLeftChange', blank=True,
                                                        null=True)
    feeling_temperature_change_right = models.ForeignKey('FeelingTemperature',
                                                         related_name='FeelingTemperatureRightChange', blank=True,
                                                         null=True)

    # TODO should be n to n
    grip_study_left_cylinders_diameter = ShortFloatField(
        validators=[MinValueValidator(1), MaxValueValidator(20)])  # [cm]
    grip_study_left_weight = ShortFloatField(validators=[MinValueValidator(10), MaxValueValidator(3000)])  # [g]
    grip_study_right_cylinders_diameter = ShortFloatField(
        validators=[MinValueValidator(1), MaxValueValidator(20)])  # [cm]
    grip_study_right_weight = ShortFloatField(validators=[MinValueValidator(10), MaxValueValidator(3000)])  # [g]

    test_reflexes_left_radial = models.ForeignKey('TestReflexes', related_name='TestReflexesLeftRadial', blank=True,
                                                  null=True)
    test_reflexes_right_radial = models.ForeignKey('TestReflexes', related_name='TestReflexesRightRadial', blank=True,
                                                   null=True)

    test_reflexes_left_cubital = models.ForeignKey('TestReflexes', related_name='TestReflexesLeftCubital', blank=True,
                                                   null=True)
    test_reflexes_right_cubital = models.ForeignKey('TestReflexes', related_name='TestReflexesRightCubital', blank=True,
                                                    null=True)

    test_reflexes_left_bicephalous = models.ForeignKey('TestReflexes', related_name='TestReflexesLeftBicephalous',
                                                       blank=True, null=True)
    test_reflexes_right_bicephalous = models.ForeignKey('TestReflexes', related_name='TestReflexesRightBicephalous',
                                                        blank=True, null=True)

    test_reflexes_left_triceps = models.ForeignKey('TestReflexes', related_name='TestReflexesLeftTriceps', blank=True,
                                                   null=True)
    test_reflexes_right_triceps = models.ForeignKey('TestReflexes', related_name='TestReflexesRightTriceps', blank=True,
                                                    null=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.patient.first_name, self.patient.last_name, self.date)

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class SurfaceSense(Feature):
    pass


@verbose_names
class FeelingLimbsPose(Feature):
    pass


@verbose_names
class FeelingVibration(Feature):
    pass


@verbose_names
class FeelingPain(Feature):
    pass


@verbose_names
class FeelingTemperature(Feature):
    pass


@verbose_names
class TestReflexes(Feature):
    pass
