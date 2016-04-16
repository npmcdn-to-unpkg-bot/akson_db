from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from massage_reflexology_card.models import *


class MassageReflexologyCardCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('therapist', 'patient', 'date',),
         )}),
        (txt('Info'),
         {'fields': (('massage_reflexology_treatment', 'massage_reflexology_area'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date',)


admin.site.register(MassageReflexologyCard, MassageReflexologyCardCardAdmin)
admin.site.register(MassageReflexologyTreatment, FeatureCardAdmin)
admin.site.register(MassageReflexologyArea, FeatureCardAdmin)
