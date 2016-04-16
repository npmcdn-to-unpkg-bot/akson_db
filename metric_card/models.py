from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


@verbose_names
class MetricCard(models.Model):
    patient = models.ForeignKey(Patient)
    examiners = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    # metric
    height = ShortFloatField(validators=[MinValueValidator(100), MaxValueValidator(250)])  # [cm]
    weight = ShortFloatField(validators=[MinValueValidator(10), MaxValueValidator(250)])  # [kg]

    length_left_upper_limb_relative = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                         MaxValueValidator(
                                                                                             150)])  # [cm]
    length_left_upper_limb_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                         MaxValueValidator(
                                                                                             150)])  # [cm]
    length_left_upper_limb_real_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                              MaxValueValidator(
                                                                                                  150)])  # [cm]

    length_right_upper_limb_relative = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                          MaxValueValidator(
                                                                                              150)])  # [cm]
    length_right_upper_limb_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                          MaxValueValidator(
                                                                                              150)])  # [cm]
    length_right_upper_limb_real_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                               MaxValueValidator(
                                                                                                   150)])  # [cm]

    length_left_upper_limb_arm = ShortFloatField(blank=True, null=True,
                                                 validators=[MinValueValidator(20), MaxValueValidator(70)])  # [cm]
    length_left_upper_limb_forearm = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(20), MaxValueValidator(80)])  # [cm]
    length_left_upper_limb_hand = ShortFloatField(blank=True, null=True,
                                                  validators=[MinValueValidator(10), MaxValueValidator(50)])  # [cm]
    width_left_upper_limb_hand = ShortFloatField(blank=True, null=True,
                                                 validators=[MinValueValidator(5), MaxValueValidator(30)])  # [cm]
    length_left_upper_limb_finger = ShortFloatField(blank=True, null=True,
                                                    validators=[MinValueValidator(2), MaxValueValidator(20)])  # [cm]

    length_right_upper_limb_arm = ShortFloatField(blank=True, null=True,
                                                  validators=[MinValueValidator(20), MaxValueValidator(70)])  # [cm]
    length_right_upper_limb_forearm = ShortFloatField(blank=True, null=True,
                                                      validators=[MinValueValidator(20), MaxValueValidator(80)])  # [cm]
    length_right_upper_limb_hand = ShortFloatField(blank=True, null=True,
                                                   validators=[MinValueValidator(10), MaxValueValidator(50)])  # [cm]
    width_right_upper_limb_hand = ShortFloatField(blank=True, null=True,
                                                  validators=[MinValueValidator(5), MaxValueValidator(30)])  # [cm]
    length_right_upper_limb_finger = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(2), MaxValueValidator(20)])  # [cm]

    circuit_left_upper_limb_axillary_folds = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(5),
                                                                                                MaxValueValidator(
                                                                                                    80)])  # [cm]
    circuit_right_upper_limb_axillary_folds = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(5),
                                                                                                 MaxValueValidator(
                                                                                                     80)])  # [cm]

    circuit_left_upper_limb_15_cm_above_the_olecranon = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(5),
                                                                                    MaxValueValidator(85)])  # [cm]
    circuit_right_upper_limb_15_cm_above_the_olecranon = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(5),
                                                                                     MaxValueValidator(85)])  # [cm]

    circuit_left_upper_limb_elbow = ShortFloatField(blank=True, null=True,
                                                    validators=[MinValueValidator(5), MaxValueValidator(50)])  # [cm]
    circuit_right_upper_limb_elbow = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(5), MaxValueValidator(50)])  # [cm]

    circuit_left_upper_limb_10_cm_below_the_olecranon = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(5),
                                                                                    MaxValueValidator(50)])  # [cm]
    circuit_right_upper_limb_10_cm_below_the_olecranon = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(5),
                                                                                     MaxValueValidator(50)])  # [cm]

    circuit_left_upper_limb_radial_carpal_joint = ShortFloatField(blank=True, null=True,
                                                                  validators=[MinValueValidator(5),
                                                                              MaxValueValidator(30)])  # [cm]
    circuit_right_upper_limb_radial_carpal_joint = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(5),
                                                                               MaxValueValidator(30)])  # [cm]

    length_left_lower_limb_relative = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                         MaxValueValidator(
                                                                                             150)])  # [cm]
    length_left_lower_limb_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                         MaxValueValidator(
                                                                                             150)])  # [cm]
    length_left_lower_limb_real_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                              MaxValueValidator(
                                                                                                  150)])  # [cm]

    length_right_lower_limb_relative = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                          MaxValueValidator(
                                                                                              150)])  # [cm]
    length_right_lower_limb_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                          MaxValueValidator(
                                                                                              150)])  # [cm]
    length_right_lower_limb_real_absolute = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(50),
                                                                                               MaxValueValidator(
                                                                                                   150)])  # [cm]

    length_left_lower_limb_thigh = ShortFloatField(blank=True, null=True,
                                                   validators=[MinValueValidator(20), MaxValueValidator(80)])  # [cm]
    length_left_lower_limb_shank = ShortFloatField(blank=True, null=True,
                                                   validators=[MinValueValidator(10), MaxValueValidator(90)])  # [cm]
    length_left_lower_limb_foot = ShortFloatField(blank=True, null=True,
                                                  validators=[MinValueValidator(10), MaxValueValidator(50)])  # [cm]
    width_left_lower_limb_foot = ShortFloatField(blank=True, null=True,
                                                 validators=[MinValueValidator(5), MaxValueValidator(20)])  # [cm]

    length_right_lower_limb_thigh = ShortFloatField(blank=True, null=True,
                                                    validators=[MinValueValidator(20), MaxValueValidator(80)])  # [cm]
    length_right_lower_limb_shank = ShortFloatField(blank=True, null=True,
                                                    validators=[MinValueValidator(10), MaxValueValidator(90)])  # [cm]
    length_right_lower_limb_foot = ShortFloatField(blank=True, null=True,
                                                   validators=[MinValueValidator(10), MaxValueValidator(50)])  # [cm]
    width_right_lower_limb_foot = ShortFloatField(blank=True, null=True,
                                                  validators=[MinValueValidator(5), MaxValueValidator(20)])  # [cm]

    circuit_left_lower_limb_gluteal_fold = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(10),
                                                                                              MaxValueValidator(
                                                                                                  50)])  # [cm]
    circuit_right_lower_limb_gluteal_fold = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(10),
                                                                                               MaxValueValidator(
                                                                                                   50)])  # [cm]

    circuit_left_lower_limb_20_cm_above_the_patella = ShortFloatField(blank=True, null=True,
                                                                      validators=[MinValueValidator(10),
                                                                                  MaxValueValidator(80)])  # [cm]
    circuit_right_lower_limb_20_cm_above_the_patella = ShortFloatField(blank=True, null=True,
                                                                       validators=[MinValueValidator(10),
                                                                                   MaxValueValidator(80)])  # [cm]

    circuit_left_lower_limb_10_cm_above_the_patella = ShortFloatField(blank=True, null=True,
                                                                      validators=[MinValueValidator(10),
                                                                                  MaxValueValidator(70)])  # [cm]
    circuit_right_lower_limb_10_cm_above_the_patella = ShortFloatField(blank=True, null=True,
                                                                       validators=[MinValueValidator(10),
                                                                                   MaxValueValidator(70)])  # [cm]

    circuit_left_lower_limb_knee_joint = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(10),
                                                                                            MaxValueValidator(
                                                                                                40)])  # [cm]
    circuit_right_lower_limb_knee_joint = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(10),
                                                                                             MaxValueValidator(
                                                                                                 40)])  # [cm]

    circuit_left_lower_limb_15_cm_below_the_patella = ShortFloatField(blank=True, null=True,
                                                                      validators=[MinValueValidator(10),
                                                                                  MaxValueValidator(70)])  # [cm]
    circuit_right_lower_limb_15_cm_below_the_patella = ShortFloatField(blank=True, null=True,
                                                                       validators=[MinValueValidator(10),
                                                                                   MaxValueValidator(70)])  # [cm]

    circuit_left_lower_limb_ankle = ShortFloatField(blank=True, null=True,
                                                    validators=[MinValueValidator(5), MaxValueValidator(35)])  # [cm]
    circuit_right_lower_limb_ankle = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(5), MaxValueValidator(35)])  # [cm]

    range_left_active_motion_shoulder_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            70)])  # [stopnie]
    range_left_active_motion_shoulder_joint_bending = ShortFloatField(blank=True, null=True,
                                                                      validators=[MinValueValidator(0),
                                                                                  MaxValueValidator(190)])  # [stopnie]

    range_left_active_motion_shoulder_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(0),
                                                                                    MaxValueValidator(
                                                                                        190)])  # [stopnie]
    range_left_active_motion_shoulder_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(0),
                                                                                    MaxValueValidator(40)])  # [stopnie]

    range_left_active_motion_shoulder_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                                validators=[MinValueValidator(0),
                                                                                            MaxValueValidator(
                                                                                                100)])  # [stopnie]
    range_left_active_motion_shoulder_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                                validators=[MinValueValidator(0),
                                                                                            MaxValueValidator(
                                                                                                100)])  # [stopnie]

    range_left_passive_motion_shoulder_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                             validators=[MinValueValidator(0),
                                                                                         MaxValueValidator(
                                                                                             70)])  # [stopnie]
    range_left_passive_motion_shoulder_joint_bending = ShortFloatField(blank=True, null=True,
                                                                       validators=[MinValueValidator(0),
                                                                                   MaxValueValidator(190)])  # [stopnie]

    range_left_passive_motion_shoulder_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         190)])  # [stopnie]
    range_left_passive_motion_shoulder_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         40)])  # [stopnie]

    range_left_passive_motion_shoulder_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                                 validators=[MinValueValidator(0),
                                                                                             MaxValueValidator(
                                                                                                 100)])  # [stopnie]
    range_left_passive_motion_shoulder_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                                 validators=[MinValueValidator(0),
                                                                                             MaxValueValidator(
                                                                                                 100)])  # [stopnie]

    range_left_musc_str_shoulder_joint_straightening = models.ForeignKey(
        related_name='range_left_musc_str_shoulder_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_shoulder_joint_bending = models.ForeignKey(
        related_name='range_left_musc_str_shoulder_joint_bending', to='MuscleStrength', blank=True, null=True)

    range_left_musc_str_shoulder_joint_abduction = models.ForeignKey(
        related_name='range_left_musc_str_shoulder_joint_abduction', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_shoulder_joint_adduction = models.ForeignKey(
        related_name='range_left_musc_str_shoulder_joint_adduction', to='MuscleStrength', blank=True, null=True)

    range_left_musc_str_shoulder_joint_internal_rotation = models.ForeignKey(
        related_name='range_left_musc_str_shoulder_joint_internal_rotation', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_shoulder_joint_external_rotation = models.ForeignKey(
        related_name='range_left_musc_str_shoulder_joint_external_rotation', to='MuscleStrength', blank=True, null=True)

    range_right_active_motion_shoulder_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                             validators=[MinValueValidator(0),
                                                                                         MaxValueValidator(
                                                                                             70)])  # [stopnie]
    range_right_active_motion_shoulder_joint_bending = ShortFloatField(blank=True, null=True,
                                                                       validators=[MinValueValidator(0),
                                                                                   MaxValueValidator(190)])  # [stopnie]

    range_right_active_motion_shoulder_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         190)])  # [stopnie]
    range_right_active_motion_shoulder_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         40)])  # [stopnie]

    range_right_active_motion_shoulder_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                                 validators=[MinValueValidator(0),
                                                                                             MaxValueValidator(
                                                                                                 100)])  # [stopnie]
    range_right_active_motion_shoulder_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                                 validators=[MinValueValidator(0),
                                                                                             MaxValueValidator(
                                                                                                 100)])  # [stopnie]

    range_right_passive_motion_shoulder_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                              validators=[MinValueValidator(0),
                                                                                          MaxValueValidator(
                                                                                              70)])  # [stopnie]
    range_right_passive_motion_shoulder_joint_bending = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(0),
                                                                                    MaxValueValidator(
                                                                                        190)])  # [stopnie]

    range_right_passive_motion_shoulder_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          190)])  # [stopnie]
    range_right_passive_motion_shoulder_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          40)])  # [stopnie]

    range_right_passive_motion_shoulder_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                                  validators=[MinValueValidator(0),
                                                                                              MaxValueValidator(
                                                                                                  100)])  # [stopnie]
    range_right_passive_motion_shoulder_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                                  validators=[MinValueValidator(0),
                                                                                              MaxValueValidator(
                                                                                                  100)])  # [stopnie]

    range_right_musc_str_shoulder_joint_straightening = models.ForeignKey(
        related_name='range_right_musc_str_shoulder_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_shoulder_joint_bending = models.ForeignKey(
        related_name='range_right_musc_str_shoulder_joint_bending', to='MuscleStrength', blank=True, null=True)

    range_right_musc_str_shoulder_joint_abduction = models.ForeignKey(
        related_name='range_right_musc_str_shoulder_joint_abduction', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_shoulder_joint_adduction = models.ForeignKey(
        related_name='range_right_musc_str_shoulder_joint_adduction', to='MuscleStrength', blank=True, null=True)

    range_right_musc_str_shoulder_joint_internal_rotation = models.ForeignKey(
        related_name='range_right_musc_str_shoulder_joint_internal_rotation', to='MuscleStrength', blank=True,
        null=True)
    range_right_musc_str_shoulder_joint_external_rotation = models.ForeignKey(
        related_name='range_right_musc_str_shoulder_joint_external_rotation', to='MuscleStrength', blank=True,
        null=True)

    range_left_active_motion_elbow_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         30)])  # [stopnie]
    range_left_active_motion_elbow_joint_bending = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(180)])  # [stopnie]
    range_left_passive_motion_elbow_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          30)])  # [stopnie]
    range_left_passive_motion_elbow_joint_bending = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(180)])  # [stopnie]
    range_left_musc_str_elbow_joint_straightening = models.ForeignKey(
        related_name='range_left_musc_str_elbow_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_elbow_joint_bending = models.ForeignKey(related_name='range_left_musc_str_elbow_joint_bending',
                                                                to='MuscleStrength', blank=True, null=True)

    range_right_active_motion_elbow_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          30)])  # [stopnie]
    range_right_active_motion_elbow_joint_bending = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(180)])  # [stopnie]
    range_right_passive_motion_elbow_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           30)])  # [stopnie]
    range_right_passive_motion_elbow_joint_bending = ShortFloatField(blank=True, null=True,
                                                                     validators=[MinValueValidator(0),
                                                                                 MaxValueValidator(180)])  # [stopnie]
    range_right_musc_str_elbow_joint_straightening = models.ForeignKey(
        related_name='range_right_musc_str_elbow_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_elbow_joint_bending = models.ForeignKey(
        related_name='range_right_musc_str_elbow_joint_bending', to='MuscleStrength', blank=True, null=True)

    range_left_active_motion_radial_ulnar_joint_reverse = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          100)])  # [stopnie]
    range_left_active_motion_radial_ulnar_joint_convert = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          100)])  # [stopnie]
    range_left_passive_motion_radial_ulnar_joint_reverse = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           100)])  # [stopnie]
    range_left_passive_motion_radial_ulnar_joint_convert = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           100)])  # [stopnie]
    range_left_musc_str_radial_ulnar_joint_reverse = models.ForeignKey(
        related_name='range_left_musc_str_radial_ulnar_joint_reverse', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_radial_ulnar_joint_convert = models.ForeignKey(
        related_name='range_left_musc_str_radial_ulnar_joint_convert', to='MuscleStrength', blank=True, null=True)

    range_right_active_motion_radial_ulnar_joint_reverse = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           100)])  # [stopnie]
    range_right_active_motion_radial_ulnar_joint_convert = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           100)])  # [stopnie]
    range_right_passive_motion_radial_ulnar_joint_reverse = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            100)])  # [stopnie]
    range_right_passive_motion_radial_ulnar_joint_convert = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            100)])  # [stopnie]
    range_right_musc_str_radial_ulnar_joint_reverse = models.ForeignKey(
        related_name='range_right_musc_str_radial_ulnar_joint_reverse', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_radial_ulnar_joint_convert = models.ForeignKey(
        related_name='range_right_musc_str_radial_ulnar_joint_convert', to='MuscleStrength', blank=True, null=True)

    range_left_active_motion_radial_carpal_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                    validators=[MinValueValidator(0),
                                                                                                MaxValueValidator(
                                                                                                    100)])  # [stopnie]
    range_left_active_motion_radial_carpal_joint_palmar_flexion = ShortFloatField(blank=True, null=True,
                                                                                  validators=[MinValueValidator(0),
                                                                                              MaxValueValidator(
                                                                                                  100)])  # [stopnie]
    range_left_passive_motion_radial_carpal_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                     validators=[MinValueValidator(0),
                                                                                                 MaxValueValidator(
                                                                                                     100)])  # [stopnie]
    range_left_passive_motion_radial_carpal_joint_palmar_flexion = ShortFloatField(blank=True, null=True,
                                                                                   validators=[MinValueValidator(0),
                                                                                               MaxValueValidator(
                                                                                                   100)])  # [stopnie]
    range_left_musc_str_radial_carpal_joint_extension_dorsal = models.ForeignKey(
        related_name='range_left_musc_str_radial_carpal_joint_extension_dorsal', to='MuscleStrength', blank=True,
        null=True)
    range_left_musc_str_radial_carpal_joint_palmar_flexion = models.ForeignKey(
        related_name='range_left_musc_str_radial_carpal_joint_palmar_flexion', to='MuscleStrength', blank=True,
        null=True)

    range_right_active_motion_radial_carpal_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                     validators=[MinValueValidator(0),
                                                                                                 MaxValueValidator(
                                                                                                     100)])  # [stopnie]
    range_right_active_motion_radial_carpal_joint_palmar_flexion = ShortFloatField(blank=True, null=True,
                                                                                   validators=[MinValueValidator(0),
                                                                                               MaxValueValidator(
                                                                                                   100)])  # [stopnie]
    range_right_passive_motion_radial_carpal_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                      validators=[MinValueValidator(0),
                                                                                                  MaxValueValidator(
                                                                                                      100)])  # [stopni]
    range_right_passive_motion_radial_carpal_joint_palmar_flexion = ShortFloatField(blank=True, null=True,
                                                                                    validators=[MinValueValidator(0),
                                                                                                MaxValueValidator(
                                                                                                    100)])  # [stopnie]
    range_right_musc_str_radial_carpal_joint_extension_dorsal = models.ForeignKey(
        related_name='range_right_musc_str_radial_carpal_joint_extension_dorsal', to='MuscleStrength', blank=True,
        null=True)
    range_right_musc_str_radial_carpal_joint_palmar_flexion = models.ForeignKey(
        related_name='range_right_musc_str_radial_carpal_joint_palmar_flexion', to='MuscleStrength', blank=True,
        null=True)

    range_left_active_motion_radial_carpal_joint_radial_abduction = ShortFloatField(blank=True, null=True,
                                                                                    validators=[MinValueValidator(0),
                                                                                                MaxValueValidator(
                                                                                                    45)])  # [stopnie]
    range_left_active_motion_radial_carpal_joint_urnal_abduction = ShortFloatField(blank=True, null=True,
                                                                                   validators=[MinValueValidator(0),
                                                                                               MaxValueValidator(
                                                                                                   45)])  # [stopnie]
    range_left_passive_motion_radial_carpal_joint_radial_abduction = ShortFloatField(blank=True, null=True,
                                                                                     validators=[MinValueValidator(0),
                                                                                                 MaxValueValidator(
                                                                                                     45)])  # [stopnie]
    range_left_passive_motion_radial_carpal_joint_urnal_abduction = ShortFloatField(blank=True, null=True,
                                                                                    validators=[MinValueValidator(0),
                                                                                                MaxValueValidator(
                                                                                                    45)])  # [stopnie]
    range_left_musc_str_radial_carpal_joint_radial_abduction = models.ForeignKey(
        related_name='range_left_musc_str_radial_carpal_joint_radial_abduction', to='MuscleStrength', blank=True,
        null=True)
    range_left_musc_str_radial_carpal_joint_urnal_abduction = models.ForeignKey(
        related_name='range_left_musc_str_radial_carpal_joint_urnal_abduction', to='MuscleStrength', blank=True,
        null=True)

    range_right_active_motion_radial_carpal_joint_radial_abduction = ShortFloatField(blank=True, null=True,
                                                                                     validators=[MinValueValidator(0),
                                                                                                 MaxValueValidator(
                                                                                                     45)])  # [stopnie]
    range_right_active_motion_radial_carpal_joint_urnal_abduction = ShortFloatField(blank=True, null=True,
                                                                                    validators=[MinValueValidator(0),
                                                                                                MaxValueValidator(
                                                                                                    45)])  # [stopnie]
    range_right_passive_motion_radial_carpal_joint_radial_abduction = ShortFloatField(blank=True, null=True,
                                                                                      validators=[MinValueValidator(0),
                                                                                                  MaxValueValidator(
                                                                                                      45)])  # [stopnie]
    range_right_passive_motion_radial_carpal_joint_urnal_abduction = ShortFloatField(blank=True, null=True,
                                                                                     validators=[MinValueValidator(0),
                                                                                                 MaxValueValidator(
                                                                                                     45)])  # [stopnie]
    range_right_musc_str_radial_carpal_joint_radial_abduction = models.ForeignKey(
        related_name='range_right_musc_str_radial_carpal_joint_radial_abduction', to='MuscleStrength', blank=True,
        null=True)
    range_right_musc_str_radial_carpal_joint_urnal_abduction = models.ForeignKey(
        related_name='range_right_musc_str_radial_carpal_joint_urnal_abduction', to='MuscleStrength', blank=True,
        null=True)

    range_left_active_motion_finger_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          45)])  # [stopnie]
    range_left_active_motion_finger_joint_bending = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(120)])  # [stopnie]
    range_left_passive_motion_finger_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           45)])  # [stopnie]
    range_left_passive_motion_finger_joint_bending = ShortFloatField(blank=True, null=True,
                                                                     validators=[MinValueValidator(0),
                                                                                 MaxValueValidator(120)])  # [stopnie]
    range_left_musc_str_finger_joint_straightening = models.ForeignKey(
        related_name='range_left_musc_str_finger_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_finger_joint_bending = models.ForeignKey(
        related_name='range_left_musc_str_finger_joint_bending', to='MuscleStrength', blank=True, null=True)

    range_right_active_motion_finger_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           45)])  # [stopnie]
    range_right_active_motion_finger_joint_bending = ShortFloatField(blank=True, null=True,
                                                                     validators=[MinValueValidator(0),
                                                                                 MaxValueValidator(120)])  # [stopnie]
    range_right_passive_motion_finger_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            45)])  # [stopnie]
    range_right_passive_motion_finger_joint_bending = ShortFloatField(blank=True, null=True,
                                                                      validators=[MinValueValidator(0),
                                                                                  MaxValueValidator(120)])  # [stopnie]
    range_right_musc_str_finger_joint_straightening = models.ForeignKey(
        related_name='range_right_musc_str_finger_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_finger_joint_bending = models.ForeignKey(
        related_name='range_right_musc_str_finger_joint_bending', to='MuscleStrength', blank=True, null=True)

    range_left_active_motion_hip_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                       validators=[MinValueValidator(0),
                                                                                   MaxValueValidator(45)])  # [stopnie]
    range_left_active_motion_hip_joint_bending = ShortFloatField(blank=True, null=True,
                                                                 validators=[MinValueValidator(0),
                                                                             MaxValueValidator(180)])  # [stopnie]
    range_left_active_motion_hip_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(60)])  # [stopnie]
    range_left_active_motion_hip_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(45)])  # [stopnie]
    range_left_active_motion_hip_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           60)])  # [stopnie]
    range_left_active_motion_hip_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           60)])  # [stopnie]

    range_left_passive_motion_hip_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(0),
                                                                                    MaxValueValidator(45)])  # [stopnie]
    range_left_passive_motion_hip_joint_bending = ShortFloatField(blank=True, null=True,
                                                                  validators=[MinValueValidator(0),
                                                                              MaxValueValidator(180)])  # [stopnie]
    range_left_passive_motion_hip_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(60)])  # [stopnie]
    range_left_passive_motion_hip_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(45)])  # [stopnie]
    range_left_passive_motion_hip_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            60)])  # [stopnie]
    range_left_passive_motion_hip_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            60)])  # [stopnie]

    range_left_musc_str_hip_joint_straightening = models.ForeignKey(
        related_name='range_left_musc_str_hip_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_hip_joint_bending = models.ForeignKey(related_name='range_left_musc_str_hip_joint_bending',
                                                              to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_hip_joint_abduction = models.ForeignKey(related_name='range_left_musc_str_hip_joint_abduction',
                                                                to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_hip_joint_adduction = models.ForeignKey(related_name='range_left_musc_str_hip_joint_adduction',
                                                                to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_hip_joint_internal_rotation = models.ForeignKey(
        related_name='range_left_musc_str_hip_joint_internal_rotation', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_hip_joint_external_rotation = models.ForeignKey(
        related_name='range_left_musc_str_hip_joint_external_rotation', to='MuscleStrength', blank=True, null=True)

    range_right_active_motion_hip_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(0),
                                                                                    MaxValueValidator(45)])  # [stopnie]
    range_right_active_motion_hip_joint_bending = ShortFloatField(blank=True, null=True,
                                                                  validators=[MinValueValidator(0),
                                                                              MaxValueValidator(180)])  # [stopnie]
    range_right_active_motion_hip_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(60)])  # [stopnie]
    range_right_active_motion_hip_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(45)])  # [stopnie]
    range_right_active_motion_hip_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            60)])  # [stopnie]
    range_right_active_motion_hip_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                            validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(
                                                                                            60)])  # [stopnie]

    range_right_passive_motion_hip_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         45)])  # [stopnie]
    range_right_passive_motion_hip_joint_bending = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(180)])  # [stopnie]
    range_right_passive_motion_hip_joint_abduction = ShortFloatField(blank=True, null=True,
                                                                     validators=[MinValueValidator(0),
                                                                                 MaxValueValidator(60)])  # [stopnie]
    range_right_passive_motion_hip_joint_adduction = ShortFloatField(blank=True, null=True,
                                                                     validators=[MinValueValidator(0),
                                                                                 MaxValueValidator(45)])  # [stopnie]
    range_right_passive_motion_hip_joint_internal_rotation = ShortFloatField(blank=True, null=True,
                                                                             validators=[MinValueValidator(0),
                                                                                         MaxValueValidator(
                                                                                             60)])  # [stopnie]
    range_right_passive_motion_hip_joint_external_rotation = ShortFloatField(blank=True, null=True,
                                                                             validators=[MinValueValidator(0),
                                                                                         MaxValueValidator(
                                                                                             60)])  # [stopnie]

    range_right_musc_str_hip_joint_straightening = models.ForeignKey(
        related_name='range_right_musc_str_hip_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_hip_joint_bending = models.ForeignKey(related_name='range_right_musc_str_hip_joint_bending',
                                                               to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_hip_joint_abduction = models.ForeignKey(
        related_name='range_right_musc_str_hip_joint_abduction', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_hip_joint_adduction = models.ForeignKey(
        related_name='range_right_musc_str_hip_joint_adduction', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_hip_joint_internal_rotation = models.ForeignKey(
        related_name='range_right_musc_str_hip_joint_internal_rotation', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_hip_joint_external_rotation = models.ForeignKey(
        related_name='range_right_musc_str_hip_joint_external_rotation', to='MuscleStrength', blank=True, null=True)

    range_left_active_motion_hip_joint_thomas_test = ShortFloatField(blank=True, null=True)
    range_right_active_motion_hip_joint_thomas_test = ShortFloatField(blank=True, null=True)

    range_left_active_motion_knee_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                        validators=[MinValueValidator(0),
                                                                                    MaxValueValidator(20)])  # [stopnie]
    range_left_passive_motion_knee_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         20)])  # [stopnie]
    range_left_musc_str_knee_joint_straightening = models.ForeignKey(
        related_name='range_left_musc_str_knee_joint_straightening', to='MuscleStrength', blank=True, null=True)
    range_right_active_motion_knee_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         20)])  # [stopnie]
    range_right_passive_motion_knee_joint_straightening = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          20)])  # [stopnie]
    range_right_musc_str_knee_joint_straightening = models.ForeignKey(
        related_name='range_right_musc_str_knee_joint_straightening', to='MuscleStrength', blank=True, null=True)

    range_left_active_motion_knee_joint_bending = ShortFloatField(blank=True, null=True,
                                                                  validators=[MinValueValidator(0),
                                                                              MaxValueValidator(180)])  # [stopnie]
    range_left_passive_motion_knee_joint_bending = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(180)])  # [stopnie]
    range_left_musc_str_knee_joint_bending = models.ForeignKey(related_name='range_left_musc_str_knee_joint_bending',
                                                               to='MuscleStrength', blank=True, null=True)
    range_right_active_motion_knee_joint_bending = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(180)])  # [stopnie]
    range_right_passive_motion_knee_joint_bending = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(180)])  # [stopnie]
    range_right_musc_str_knee_joint_bending = models.ForeignKey(related_name='range_right_musc_str_knee_joint_bending',
                                                                to='MuscleStrength', blank=True, null=True)

    range_left_active_motion_upper_ankle_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                  validators=[MinValueValidator(0),
                                                                                              MaxValueValidator(
                                                                                                  45)])  # [stopnie]
    range_left_active_motion_upper_ankle_joint_plantar_flexion = ShortFloatField(blank=True, null=True,
                                                                                 validators=[MinValueValidator(0),
                                                                                             MaxValueValidator(
                                                                                                 90)])  # [stopnie]
    range_left_passive_motion_upper_ankle_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                   validators=[MinValueValidator(0),
                                                                                               MaxValueValidator(
                                                                                                   45)])  # [stopnie]
    range_left_passive_motion_upper_ankle_joint_plantar_flexion = ShortFloatField(blank=True, null=True,
                                                                                  validators=[MinValueValidator(0),
                                                                                              MaxValueValidator(
                                                                                                  90)])  # [stopnie]
    range_left_musc_str_upper_ankle_joint_extension_dorsal = models.ForeignKey(
        related_name='range_left_musc_str_upper_ankle_joint_extension_dorsal', to='MuscleStrength', blank=True,
        null=True)
    range_left_musc_str_upper_ankle_joint_plantar_flexion = models.ForeignKey(
        related_name='range_left_musc_str_upper_ankle_joint_plantar_flexion', to='MuscleStrength', blank=True,
        null=True)

    range_right_active_motion_upper_ankle_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                   validators=[MinValueValidator(0),
                                                                                               MaxValueValidator(
                                                                                                   45)])  # [stopnie]
    range_right_active_motion_upper_ankle_joint_plantar_flexion = ShortFloatField(blank=True, null=True,
                                                                                  validators=[MinValueValidator(0),
                                                                                              MaxValueValidator(
                                                                                                  90)])  # [stopnie]
    range_right_passive_motion_upper_ankle_joint_extension_dorsal = ShortFloatField(blank=True, null=True,
                                                                                    validators=[MinValueValidator(0),
                                                                                                MaxValueValidator(
                                                                                                    45)])  # [stopnie]
    range_right_passive_motion_upper_ankle_joint_plantar_flexion = ShortFloatField(blank=True, null=True,
                                                                                   validators=[MinValueValidator(0),
                                                                                               MaxValueValidator(
                                                                                                   90)])  # [stopnie]
    range_right_musc_str_upper_ankle_joint_extension_dorsal = models.ForeignKey(
        related_name='range_right_musc_str_upper_ankle_joint_extension_dorsal', to='MuscleStrength', blank=True,
        null=True)
    range_right_musc_str_upper_ankle_joint_plantar_flexion = models.ForeignKey(
        related_name='range_right_musc_str_upper_ankle_joint_plantar_flexion', to='MuscleStrength', blank=True,
        null=True)

    range_left_active_motion_lower_ankle_joint_reverse = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         60)])  # [stopnie]
    range_left_active_motion_lower_ankle_joint_convert = ShortFloatField(blank=True, null=True,
                                                                         validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(
                                                                                         35)])  # [stopnie]
    range_left_passive_motion_lower_ankle_joint_reverse = ShortFloatField(blank=True, null=True)
    range_left_passive_motion_lower_ankle_joint_convert = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          35)])  # [stopnie]
    range_left_musc_str_lower_ankle_joint_reverse = models.ForeignKey(
        related_name='range_left_musc_str_lower_ankle_joint_reverse', to='MuscleStrength', blank=True, null=True)
    range_left_musc_str_lower_ankle_joint_convert = models.ForeignKey(
        related_name='range_left_musc_str_lower_ankle_joint_convert', to='MuscleStrength', blank=True, null=True)

    range_right_active_motion_lower_ankle_joint_reverse = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          60)])  # [stopnie]
    range_right_active_motion_lower_ankle_joint_convert = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(
                                                                                          35)])  # [stopnie]
    range_right_passive_motion_lower_ankle_joint_reverse = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           60)])  # [stopnie]
    range_right_passive_motion_lower_ankle_joint_convert = ShortFloatField(blank=True, null=True,
                                                                           validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(
                                                                                           35)])  # [stopnie]
    range_right_musc_str_lower_ankle_joint_reverse = models.ForeignKey(
        related_name='range_right_musc_str_lower_ankle_joint_reverse', to='MuscleStrength', blank=True, null=True)
    range_right_musc_str_lower_ankle_joint_convert = models.ForeignKey(
        related_name='range_right_musc_str_lower_ankle_joint_convert', to='MuscleStrength', blank=True, null=True)

    sftr_S_cervical_sftr_extension = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(0), MaxValueValidator(50)])
    sftr_S_cervical_sftr_bend = ShortFloatField(blank=True, null=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(50)])

    sftr_F_cervical_sftr_left_slope = ShortFloatField(blank=True, null=True,
                                                      validators=[MinValueValidator(0), MaxValueValidator(55)])
    sftr_F_cervical_sftr_right_slope = ShortFloatField(blank=True, null=True,
                                                       validators=[MinValueValidator(0), MaxValueValidator(55)])

    sftr_R_cervical_sftr_left_rotation = ShortFloatField(blank=True, null=True,
                                                         validators=[MinValueValidator(0), MaxValueValidator(60)])
    sftr_R_cervical_sftr_right_rotation = ShortFloatField(blank=True, null=True,
                                                          validators=[MinValueValidator(0), MaxValueValidator(60)])

    sftr_S_thoraco_lumbar_sftr_extension = ShortFloatField(blank=True, null=True,
                                                           validators=[MinValueValidator(0), MaxValueValidator(40)])
    sftr_S_thoraco_lumbar_sftr_bend = ShortFloatField(blank=True, null=True,
                                                      validators=[MinValueValidator(0), MaxValueValidator(95)])

    sftr_F_thoraco_lumbar_sftr_left_slope = ShortFloatField(blank=True, null=True,
                                                            validators=[MinValueValidator(0), MaxValueValidator(40)])
    sftr_F_thoraco_lumbar_sftr_right_slope = ShortFloatField(blank=True, null=True,
                                                             validators=[MinValueValidator(0), MaxValueValidator(40)])

    sftr_R_thoraco_lumbar_sftr_left_rotation = ShortFloatField(blank=True, null=True,
                                                               validators=[MinValueValidator(0), MaxValueValidator(55)])
    sftr_R_thoraco_lumbar_sftr_right_rotation = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(0),
                                                                                                   MaxValueValidator(
                                                                                                       55)])

    sftr_S_shoulder_sftr_extension = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(0), MaxValueValidator(60)])
    sftr_S_shoulder_sftr_bend = ShortFloatField(blank=True, null=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(185)])

    sftr_F_shoulder_sftr_abduction = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(0), MaxValueValidator(185)])
    sftr_F_shoulder_sftr_adduction = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(0), MaxValueValidator(10)])

    sftr_T_shoulder_sftr_horizontal_plane_extension = ShortFloatField(blank=True, null=True,
                                                                      validators=[MinValueValidator(0),
                                                                                  MaxValueValidator(40)])
    sftr_T_shoulder_sftr_horizontal_plane_bend = ShortFloatField(blank=True, null=True,
                                                                 validators=[MinValueValidator(0),
                                                                             MaxValueValidator(150)])

    sftr_RF0_shoulder_sftr_outter_rotation = ShortFloatField(blank=True, null=True,
                                                             validators=[MinValueValidator(0), MaxValueValidator(70)])
    sftr_RF0_shoulder_sftr_inner_rotation = ShortFloatField(blank=True, null=True,
                                                            validators=[MinValueValidator(0), MaxValueValidator(80)])

    sftr_RF90_shoulder_sftr_outter_rotation = ShortFloatField(blank=True, null=True,
                                                              validators=[MinValueValidator(0), MaxValueValidator(100)])
    sftr_RF90_shoulder_sftr_inner_rotation = ShortFloatField(blank=True, null=True,
                                                             validators=[MinValueValidator(0), MaxValueValidator(90)])

    sftr_S_elbow_sftr_extension = ShortFloatField(blank=True, null=True,
                                                  validators=[MinValueValidator(0), MaxValueValidator(10)])
    sftr_S_elbow_sftr_bend = ShortFloatField(blank=True, null=True,
                                             validators=[MinValueValidator(0), MaxValueValidator(165)])

    sftr_R_radial_ulnar_nearer_and_further_sftr_reverse = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(100)])
    sftr_R_radial_ulnar_nearer_and_further_sftr_convert = ShortFloatField(blank=True, null=True,
                                                                          validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(90)])

    sftr_S_radial_carpal_sftr_extension = ShortFloatField(blank=True, null=True,
                                                          validators=[MinValueValidator(0), MaxValueValidator(60)])
    sftr_S_radial_carpal_sftr_bend = ShortFloatField(blank=True, null=True,
                                                     validators=[MinValueValidator(0), MaxValueValidator(70)])

    sftr_F_radial_carpal_sftr_radial_abduction = ShortFloatField(blank=True, null=True,
                                                                 validators=[MinValueValidator(0),
                                                                             MaxValueValidator(30)])
    sftr_F_radial_carpal_sftr_elbow_abduction = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(0),
                                                                                                   MaxValueValidator(
                                                                                                       40)])

    sftr_VF_carpo_metacarpal_sftr_inradial_abduction = ShortFloatField(blank=True, null=True,
                                                                       validators=[MinValueValidator(0),
                                                                                   MaxValueValidator(40)])
    sftr_VF_carpo_metacarpal_sftr_inelbow_adduction = ShortFloatField(blank=True, null=True,
                                                                      validators=[MinValueValidator(0),
                                                                                  MaxValueValidator(25)])

    sftr_VS_carpo_metacarpal_sftr_hand_abduction = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(50)])
    sftr_VS_carpo_metacarpal_sftr_hand_adduction = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(10)])

    sftr_CR_carpo_metacarpal_sftr_guided = ShortFloatField(blank=True, null=True,
                                                           validators=[MinValueValidator(0), MaxValueValidator(30)])
    sftr_CR_carpo_metacarpal_sftr_enclose = ShortFloatField(blank=True, null=True,
                                                            validators=[MinValueValidator(0), MaxValueValidator(105)])

    sftr_S_metacarpal_finger1_sftr_extension = ShortFloatField(blank=True, null=True,
                                                               validators=[MinValueValidator(0), MaxValueValidator(15)])
    sftr_S_metacarpal_finger1_sftr_bend = ShortFloatField(blank=True, null=True,
                                                          validators=[MinValueValidator(0), MaxValueValidator(60)])

    sftr_S_metacarpal_finger2_sftr_extension = ShortFloatField(blank=True, null=True,
                                                               validators=[MinValueValidator(0), MaxValueValidator(40)])
    sftr_S_metacarpal_finger2_sftr_bend = ShortFloatField(blank=True, null=True,
                                                          validators=[MinValueValidator(0), MaxValueValidator(105)])

    sftr_F_metacarpal_finger2_sftr_abduction = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(0),
                                                                                                  MaxValueValidator(
                                                                                                      45)])  # [stopnie]
    sftr_F_metacarpal_finger2_sftr_adduction = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(0),
                                                                                                  MaxValueValidator(
                                                                                                      45)])  # [stopnie]

    sftr_S_interphalangeal_sftr_extension = ShortFloatField(blank=True, null=True,
                                                            validators=[MinValueValidator(0), MaxValueValidator(25)])
    sftr_S_interphalangeal_sftr_bend = ShortFloatField(blank=True, null=True,
                                                       validators=[MinValueValidator(0), MaxValueValidator(100)])

    sftr_S_interphalangeal_nearer_sftr_extension = ShortFloatField(blank=True, null=True,
                                                                   validators=[MinValueValidator(0),
                                                                               MaxValueValidator(10)])
    sftr_S_interphalangeal_nearer_sftr_bend = ShortFloatField(blank=True, null=True,
                                                              validators=[MinValueValidator(0), MaxValueValidator(115)])

    sftr_S_interphalangeal_further_sftr_extension = ShortFloatField(blank=True, null=True,
                                                                    validators=[MinValueValidator(0),
                                                                                MaxValueValidator(10)])
    sftr_S_interphalangeal_further_sftr_bend = ShortFloatField(blank=True, null=True,
                                                               validators=[MinValueValidator(0), MaxValueValidator(90)])

    sftr_S_hip_sftr_extension = ShortFloatField(blank=True, null=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(25)])
    sftr_S_hip_sftr_bend = ShortFloatField(blank=True, null=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(140)])

    sftr_F_hip_sftr_abduction = ShortFloatField(blank=True, null=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(55)])
    sftr_F_hip_sftr_adduction = ShortFloatField(blank=True, null=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(35)])

    sftr_RS90_hip_sftr_outter_rotation = ShortFloatField(blank=True, null=True,
                                                         validators=[MinValueValidator(0), MaxValueValidator(55)])
    sftr_RS90_hip_sftr_inner_rotation = ShortFloatField(blank=True, null=True,
                                                        validators=[MinValueValidator(0), MaxValueValidator(55)])

    sftr_RS0_hip_sftr_outter_rotation = ShortFloatField(blank=True, null=True,
                                                        validators=[MinValueValidator(0), MaxValueValidator(55)])
    sftr_RS0_hip_sftr_inner_rotation = ShortFloatField(blank=True, null=True,
                                                       validators=[MinValueValidator(0), MaxValueValidator(50)])

    sftr_S_knee_sftr_extension = ShortFloatField(blank=True, null=True,
                                                 validators=[MinValueValidator(0), MaxValueValidator(10)])
    sftr_S_knee_sftr_bend = ShortFloatField(blank=True, null=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(140)])

    sftr_S_angle_upper_and_lower_sftr_extension = ShortFloatField(blank=True, null=True,
                                                                  validators=[MinValueValidator(0),
                                                                              MaxValueValidator(30)])
    sftr_S_angle_upper_and_lower_sftr_bend = ShortFloatField(blank=True, null=True,
                                                             validators=[MinValueValidator(0), MaxValueValidator(55)])

    sftr_R_angle_upper_and_lower_sftr_convert = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(0),
                                                                                                   MaxValueValidator(
                                                                                                       30)])
    sftr_R_angle_upper_and_lower_sftr_reverse = ShortFloatField(blank=True, null=True, validators=[MinValueValidator(0),
                                                                                                   MaxValueValidator(
                                                                                                       50)])

    additional_notes = AdditionalNotesField(blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.patient.first_name, self.patient.last_name, self.date)

    class Meta:
        ordering = ['date']


@verbose_names
class MuscleStrength(Feature):
    pass
