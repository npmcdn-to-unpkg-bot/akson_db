from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from metric_card.models import *


class MetricCardCardAdmin(AksonCardAdmin):
    add_form_template = 'metric_card.html'

    fieldsets = (
        (txt('General'),
         {'fields': (('patient', 'examiners', 'date'),
                     )}),
        (txt('Basic metrics'),
         {'fields': (('height', 'weight'),
                     )}),
        # part
        ('Upper limb',
         {'description': 'Limbs measures',
          'fields': (
              ('length_left_upper_limb_relative', 'length_right_upper_limb_relative'),
              ('length_left_upper_limb_absolute', 'length_right_upper_limb_absolute'),
              ('length_left_upper_limb_real_absolute', 'length_right_upper_limb_real_absolute'),
              ('length_left_upper_limb_arm', 'length_right_upper_limb_arm'),
              ('length_left_upper_limb_forearm', 'length_right_upper_limb_forearm'),
              ('length_left_upper_limb_hand', 'length_right_upper_limb_hand'),
              ('width_left_upper_limb_hand', 'width_right_upper_limb_hand'),
              ('length_left_upper_limb_finger', 'length_right_upper_limb_finger'),
              ('circuit_left_upper_limb_axillary_folds', 'circuit_right_upper_limb_axillary_folds'),
              ('circuit_left_upper_limb_15_cm_above_the_olecranon',
               'circuit_right_upper_limb_15_cm_above_the_olecranon'),
              ('circuit_left_upper_limb_elbow', 'circuit_right_upper_limb_elbow'),
              ('circuit_left_upper_limb_10_cm_below_the_olecranon',
               'circuit_right_upper_limb_10_cm_below_the_olecranon'),
              ('circuit_left_upper_limb_radial_carpal_joint', 'circuit_right_upper_limb_radial_carpal_joint'),
          )}),
        ('Lower limb',
         {'fields': (
             ('length_left_lower_limb_relative', 'length_right_lower_limb_relative'),
             ('length_left_lower_limb_absolute', 'length_right_lower_limb_absolute'),
             ('length_left_lower_limb_real_absolute', 'length_right_lower_limb_real_absolute'),
             ('length_left_lower_limb_thigh', 'length_right_lower_limb_thigh'),
             ('length_left_lower_limb_shank', 'length_right_lower_limb_shank'),
             ('length_left_lower_limb_foot', 'length_right_lower_limb_foot'),
             ('width_left_lower_limb_foot', 'width_right_lower_limb_foot'),
             ('circuit_left_lower_limb_gluteal_fold', 'circuit_right_lower_limb_gluteal_fold'),
             ('circuit_left_lower_limb_20_cm_above_the_patella', 'circuit_right_lower_limb_20_cm_above_the_patella'),
             ('circuit_left_lower_limb_10_cm_above_the_patella', 'circuit_right_lower_limb_10_cm_above_the_patella'),
             ('circuit_left_lower_limb_knee_joint', 'circuit_right_lower_limb_knee_joint'),
             ('circuit_left_lower_limb_15_cm_below_the_patella', 'circuit_right_lower_limb_15_cm_below_the_patella'),
             ('circuit_left_lower_limb_ankle', 'circuit_right_lower_limb_ankle'),
         )}),
        # part
        ('Shoulder joint',
         {'description': 'Upper limb motion and strength',
          'fields': (
              ('range_left_active_motion_shoulder_joint_straightening',
               'range_left_passive_motion_shoulder_joint_straightening',
               'range_left_musc_str_shoulder_joint_straightening',
               'range_right_active_motion_shoulder_joint_straightening',
               'range_right_passive_motion_shoulder_joint_straightening',
               'range_right_musc_str_shoulder_joint_straightening'),
              ('range_left_active_motion_shoulder_joint_bending', 'range_left_passive_motion_shoulder_joint_bending',
               'range_left_musc_str_shoulder_joint_bending', 'range_right_active_motion_shoulder_joint_bending',
               'range_right_passive_motion_shoulder_joint_bending', 'range_right_musc_str_shoulder_joint_bending'),
              ('range_left_active_motion_shoulder_joint_abduction',
               'range_left_passive_motion_shoulder_joint_abduction',
               'range_left_musc_str_shoulder_joint_abduction', 'range_right_active_motion_shoulder_joint_abduction',
               'range_right_passive_motion_shoulder_joint_abduction',
               'range_right_musc_str_shoulder_joint_abduction'),
              ('range_left_active_motion_shoulder_joint_adduction',
               'range_left_passive_motion_shoulder_joint_adduction',
               'range_left_musc_str_shoulder_joint_adduction', 'range_right_active_motion_shoulder_joint_adduction',
               'range_right_passive_motion_shoulder_joint_adduction',
               'range_right_musc_str_shoulder_joint_adduction'),
              ('range_left_active_motion_shoulder_joint_internal_rotation',
               'range_left_passive_motion_shoulder_joint_internal_rotation',
               'range_left_musc_str_shoulder_joint_internal_rotation',
               'range_right_active_motion_shoulder_joint_internal_rotation',
               'range_right_passive_motion_shoulder_joint_internal_rotation',
               'range_right_musc_str_shoulder_joint_internal_rotation'),
              ('range_left_active_motion_shoulder_joint_external_rotation',
               'range_left_passive_motion_shoulder_joint_external_rotation',
               'range_left_musc_str_shoulder_joint_external_rotation',
               'range_right_active_motion_shoulder_joint_external_rotation',
               'range_right_passive_motion_shoulder_joint_external_rotation',
               'range_right_musc_str_shoulder_joint_external_rotation'),
          )}),
        # part
        ('elbow_joint',
         {'fields': (
             ('range_left_active_motion_elbow_joint_straightening',
              'range_left_passive_motion_elbow_joint_straightening', 'range_left_musc_str_elbow_joint_straightening',
              'range_right_active_motion_elbow_joint_straightening',
              'range_right_passive_motion_elbow_joint_straightening', 'range_right_musc_str_elbow_joint_straightening'),
             ('range_left_active_motion_elbow_joint_bending', 'range_left_passive_motion_elbow_joint_bending',
              'range_left_musc_str_elbow_joint_bending', 'range_right_active_motion_elbow_joint_bending',
              'range_right_passive_motion_elbow_joint_bending', 'range_right_musc_str_elbow_joint_bending'),
         )}),
        # part
        ('radial_ulnar_joint',
         {'fields': (
             ('range_left_active_motion_radial_ulnar_joint_reverse',
              'range_left_passive_motion_radial_ulnar_joint_reverse', 'range_left_musc_str_radial_ulnar_joint_reverse',
              'range_right_active_motion_radial_ulnar_joint_reverse',
              'range_right_passive_motion_radial_ulnar_joint_reverse',
              'range_right_musc_str_radial_ulnar_joint_reverse'),
             ('range_left_active_motion_radial_ulnar_joint_convert',
              'range_left_passive_motion_radial_ulnar_joint_convert', 'range_left_musc_str_radial_ulnar_joint_convert',
              'range_right_active_motion_radial_ulnar_joint_convert',
              'range_right_passive_motion_radial_ulnar_joint_convert',
              'range_right_musc_str_radial_ulnar_joint_convert'),
         )}),
        # part
        ('radial_carpal_joint',
         {'fields': (
             ('range_left_active_motion_radial_carpal_joint_extension_dorsal',
              'range_left_passive_motion_radial_carpal_joint_extension_dorsal',
              'range_left_musc_str_radial_carpal_joint_extension_dorsal',
              'range_right_active_motion_radial_carpal_joint_extension_dorsal',
              'range_right_passive_motion_radial_carpal_joint_extension_dorsal',
              'range_right_musc_str_radial_carpal_joint_extension_dorsal'),
             ('range_left_active_motion_radial_carpal_joint_palmar_flexion',
              'range_left_passive_motion_radial_carpal_joint_palmar_flexion',
              'range_left_musc_str_radial_carpal_joint_palmar_flexion',
              'range_right_active_motion_radial_carpal_joint_palmar_flexion',
              'range_right_passive_motion_radial_carpal_joint_palmar_flexion',
              'range_right_musc_str_radial_carpal_joint_palmar_flexion'),
             ('range_left_active_motion_radial_carpal_joint_radial_abduction',
              'range_left_passive_motion_radial_carpal_joint_radial_abduction',
              'range_left_musc_str_radial_carpal_joint_radial_abduction',
              'range_right_active_motion_radial_carpal_joint_radial_abduction',
              'range_right_passive_motion_radial_carpal_joint_radial_abduction',
              'range_right_musc_str_radial_carpal_joint_radial_abduction'),
             ('range_left_active_motion_radial_carpal_joint_urnal_abduction',
              'range_left_passive_motion_radial_carpal_joint_urnal_abduction',
              'range_left_musc_str_radial_carpal_joint_urnal_abduction',
              'range_right_active_motion_radial_carpal_joint_urnal_abduction',
              'range_right_passive_motion_radial_carpal_joint_urnal_abduction',
              'range_right_musc_str_radial_carpal_joint_urnal_abduction'),
         )}),
        # part
        ('finger_joint',
         {'fields': (
             ('range_left_active_motion_finger_joint_straightening',
              'range_left_passive_motion_finger_joint_straightening', 'range_left_musc_str_finger_joint_straightening',
              'range_right_active_motion_finger_joint_straightening',
              'range_right_passive_motion_finger_joint_straightening',
              'range_right_musc_str_finger_joint_straightening'),
             ('range_left_active_motion_finger_joint_bending', 'range_left_passive_motion_finger_joint_bending',
              'range_left_musc_str_finger_joint_bending', 'range_right_active_motion_finger_joint_bending',
              'range_right_passive_motion_finger_joint_bending', 'range_right_musc_str_finger_joint_bending'),
         )}),

        # part
        ('Hip joint',
         {'description': 'Lower limb motion and strength',
          'fields': (
              ('range_left_active_motion_hip_joint_straightening', 'range_left_passive_motion_hip_joint_straightening',
               'range_left_musc_str_hip_joint_straightening', 'range_right_active_motion_hip_joint_straightening',
               'range_right_passive_motion_hip_joint_straightening', 'range_right_musc_str_hip_joint_straightening'),
              ('range_left_active_motion_hip_joint_bending', 'range_left_passive_motion_hip_joint_bending',
               'range_left_musc_str_hip_joint_bending', 'range_right_active_motion_hip_joint_bending',
               'range_right_passive_motion_hip_joint_bending', 'range_right_musc_str_hip_joint_bending'),
              ('range_left_active_motion_hip_joint_abduction', 'range_left_passive_motion_hip_joint_abduction',
               'range_left_musc_str_hip_joint_abduction', 'range_right_active_motion_hip_joint_abduction',
               'range_right_passive_motion_hip_joint_abduction', 'range_right_musc_str_hip_joint_abduction'),
              ('range_left_active_motion_hip_joint_adduction', 'range_left_passive_motion_hip_joint_adduction',
               'range_left_musc_str_hip_joint_adduction', 'range_right_active_motion_hip_joint_adduction',
               'range_right_passive_motion_hip_joint_adduction', 'range_right_musc_str_hip_joint_adduction'),
              ('range_left_active_motion_hip_joint_internal_rotation',
               'range_left_passive_motion_hip_joint_internal_rotation',
               'range_left_musc_str_hip_joint_internal_rotation',
               'range_right_active_motion_hip_joint_internal_rotation',
               'range_right_passive_motion_hip_joint_internal_rotation',
               'range_right_musc_str_hip_joint_internal_rotation'),
              ('range_left_active_motion_hip_joint_external_rotation',
               'range_left_passive_motion_hip_joint_external_rotation',
               'range_left_musc_str_hip_joint_external_rotation',
               'range_right_active_motion_hip_joint_external_rotation',
               'range_right_passive_motion_hip_joint_external_rotation',
               'range_right_musc_str_hip_joint_external_rotation'),
              ('range_left_active_motion_hip_joint_thomas_test', 'range_right_active_motion_hip_joint_thomas_test',),
          )}),
        # part
        ('knee_joint',
         {'fields': (
             ('range_left_active_motion_knee_joint_straightening', 'range_left_passive_motion_knee_joint_straightening',
              'range_left_musc_str_knee_joint_straightening', 'range_right_active_motion_knee_joint_straightening',
              'range_right_passive_motion_knee_joint_straightening', 'range_right_musc_str_knee_joint_straightening'),
             ('range_left_active_motion_knee_joint_bending', 'range_left_passive_motion_knee_joint_bending',
              'range_left_musc_str_knee_joint_bending', 'range_right_active_motion_knee_joint_bending',
              'range_right_passive_motion_knee_joint_bending', 'range_right_musc_str_knee_joint_bending'),
         )}),
        # part
        ('upper_ankle_joint',
         {'fields': (
             ('range_left_active_motion_upper_ankle_joint_extension_dorsal',
              'range_left_passive_motion_upper_ankle_joint_extension_dorsal',
              'range_left_musc_str_upper_ankle_joint_extension_dorsal',
              'range_right_active_motion_upper_ankle_joint_extension_dorsal',
              'range_right_passive_motion_upper_ankle_joint_extension_dorsal',
              'range_right_musc_str_upper_ankle_joint_extension_dorsal'),
             ('range_left_active_motion_upper_ankle_joint_plantar_flexion',
              'range_left_passive_motion_upper_ankle_joint_plantar_flexion',
              'range_left_musc_str_upper_ankle_joint_plantar_flexion',
              'range_right_active_motion_upper_ankle_joint_plantar_flexion',
              'range_right_passive_motion_upper_ankle_joint_plantar_flexion',
              'range_right_musc_str_upper_ankle_joint_plantar_flexion'),
         )}),
        # part
        ('lower_ankle_joint',
         {'fields': (
             ('range_left_active_motion_lower_ankle_joint_convert',
              'range_left_passive_motion_lower_ankle_joint_convert', 'range_left_musc_str_lower_ankle_joint_convert',
              'range_right_active_motion_lower_ankle_joint_convert',
              'range_right_passive_motion_lower_ankle_joint_convert', 'range_right_musc_str_lower_ankle_joint_convert'),
             ('range_left_active_motion_lower_ankle_joint_reverse',
              'range_left_passive_motion_lower_ankle_joint_reverse', 'range_left_musc_str_lower_ankle_joint_reverse',
              'range_right_active_motion_lower_ankle_joint_reverse',
              'range_right_passive_motion_lower_ankle_joint_reverse', 'range_right_musc_str_lower_ankle_joint_reverse'),
         )}),
        # part
        ('cervical_sftr',
         {'description': 'SFTR measures',
          'fields': (
              ('sftr_S_cervical_sftr_extension', 'sftr_S_cervical_sftr_bend'),
              ('sftr_F_cervical_sftr_left_slope', 'sftr_F_cervical_sftr_right_slope'),
              ('sftr_R_cervical_sftr_left_rotation', 'sftr_R_cervical_sftr_right_rotation'),
          )}),
        ('thoraco_lumbar_sftr',
         {'fields': (
             ('sftr_S_thoraco_lumbar_sftr_extension', 'sftr_S_thoraco_lumbar_sftr_bend'),
             ('sftr_F_thoraco_lumbar_sftr_left_slope', 'sftr_F_thoraco_lumbar_sftr_right_slope'),
             ('sftr_R_thoraco_lumbar_sftr_left_rotation', 'sftr_R_thoraco_lumbar_sftr_right_rotation'),
         )}),
        ('shoulder_sftr',
         {'fields': (
             ('sftr_S_shoulder_sftr_extension', 'sftr_S_shoulder_sftr_bend'),
             ('sftr_F_shoulder_sftr_abduction', 'sftr_F_shoulder_sftr_adduction'),
             ('sftr_T_shoulder_sftr_horizontal_plane_extension', 'sftr_T_shoulder_sftr_horizontal_plane_bend'),
             ('sftr_RF0_shoulder_sftr_outter_rotation', 'sftr_RF0_shoulder_sftr_inner_rotation'),
             ('sftr_RF90_shoulder_sftr_outter_rotation', 'sftr_RF90_shoulder_sftr_inner_rotation'),
         )}),
        ('elbow_sftr',
         {'fields': (
             ('sftr_S_elbow_sftr_extension', 'sftr_S_elbow_sftr_bend'),
         )}),
        ('radial_ulnar_nearer_and_further_sftr',
         {'fields': (
             ('sftr_R_radial_ulnar_nearer_and_further_sftr_reverse',
              'sftr_R_radial_ulnar_nearer_and_further_sftr_convert'),
         )}),
        ('radial_carpal_sftr',
         {'fields': (
             ('sftr_S_radial_carpal_sftr_extension', 'sftr_S_radial_carpal_sftr_bend'),
             ('sftr_F_radial_carpal_sftr_radial_abduction', 'sftr_F_radial_carpal_sftr_elbow_abduction'),
         )}),
        ('carpo_metacarpal_sftr',
         {'fields': (
             ('sftr_VF_carpo_metacarpal_sftr_inradial_abduction', 'sftr_VF_carpo_metacarpal_sftr_inelbow_adduction'),
             ('sftr_VS_carpo_metacarpal_sftr_hand_abduction', 'sftr_VS_carpo_metacarpal_sftr_hand_adduction'),
             ('sftr_CR_carpo_metacarpal_sftr_guided', 'sftr_CR_carpo_metacarpal_sftr_enclose'),
         )}),
        ('metacarpal_finger1_sftr',
         {'fields': (
             ('sftr_S_metacarpal_finger1_sftr_extension', 'sftr_S_metacarpal_finger1_sftr_bend'),
         )}),
        ('metacarpal_finger2_sftr',
         {'fields': (
             ('sftr_S_metacarpal_finger2_sftr_extension', 'sftr_S_metacarpal_finger2_sftr_bend'),
             ('sftr_F_metacarpal_finger2_sftr_abduction', 'sftr_F_metacarpal_finger2_sftr_adduction'),
         )}),
        ('interphalangeal_sftr',
         {'fields': (
             ('sftr_S_interphalangeal_sftr_extension', 'sftr_S_interphalangeal_sftr_bend'),
         )}),
        ('interphalangeal_nearer_sftr',
         {'fields': (
             ('sftr_S_interphalangeal_nearer_sftr_extension', 'sftr_S_interphalangeal_nearer_sftr_bend'),
         )}),
        ('interphalangeal_further_sftr',
         {'fields': (
             ('sftr_S_interphalangeal_further_sftr_extension', 'sftr_S_interphalangeal_further_sftr_bend'),
         )}),
        ('hip_sftr',
         {'fields': (
             ('sftr_S_hip_sftr_extension', 'sftr_S_hip_sftr_bend'),
             ('sftr_F_hip_sftr_abduction', 'sftr_F_hip_sftr_adduction'),
             ('sftr_RS90_hip_sftr_outter_rotation', 'sftr_RS90_hip_sftr_inner_rotation'),
             ('sftr_RS0_hip_sftr_outter_rotation', 'sftr_RS0_hip_sftr_inner_rotation'),
         )}),
        ('knee_sftr',
         {'fields': (
             ('sftr_S_knee_sftr_extension', 'sftr_S_knee_sftr_bend'),
         )}),
        ('angle_upper_and_lower_sftr',
         {'fields': (
             ('sftr_S_angle_upper_and_lower_sftr_extension', 'sftr_S_angle_upper_and_lower_sftr_bend'),
             ('sftr_R_angle_upper_and_lower_sftr_convert', 'sftr_R_angle_upper_and_lower_sftr_reverse'),
         )}),

        (txt('Additionals'),
         {'fields': (
             ('additional_notes',),
         )}),
    )

    list_display = ('patient', 'date',)


admin.site.register(MetricCard, MetricCardCardAdmin)
admin.site.register(MuscleStrength, FeatureCardAdmin)