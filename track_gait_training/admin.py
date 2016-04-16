from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from track_gait_training.models import *


class TrackGaitTrainingCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('leading_people', 'patient', 'date',),
         )}),
        (txt('Blood pressure at rest'),
         {'fields': (('blood_pressure_hr_rest', 'blood_pressure_rr_sys', 'blood_pressure_rr_dia'),
                     )}),
        (txt('Helpers'),
         {'fields': (('support_type', 'left_orthosis', 'right_orthosis'),
                     )}),
        (txt('Results'),
         {'fields': (('restoration_time', 'gait_speed', 'gait_time', 'fixation_location', 'load'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date', 'restoration_time', 'gait_speed')


admin.site.register(TrackGaitTraining, TrackGaitTrainingCardAdmin)
admin.site.register(FixationLocation, FeatureCardAdmin)
admin.site.register(SupportType, FeatureCardAdmin)
