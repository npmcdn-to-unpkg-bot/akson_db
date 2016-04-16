from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from upper_limb_therapy.models import *


class UpperLimbTherapyCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('therapist', 'patient', 'date',),
         )}),
        (txt('Therapy info'),
         {'fields': (('therapy_detailed_target', 'left_area', 'right_area', 'used_methods_techniques'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date',)


admin.site.register(UpperLimbTherapy, UpperLimbTherapyCardAdmin)
admin.site.register(TherapyDetailedTarget, FeatureCardAdmin)
admin.site.register(TherapyArea, FeatureCardAdmin)
admin.site.register(TherapyUsedMethodsTechniques, FeatureCardAdmin)
