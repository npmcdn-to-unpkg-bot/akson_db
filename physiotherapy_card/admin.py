from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from physiotherapy_card.models import *


class PhysiotherapyCardCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'), 
            {'fields': (
                ('leading_people', 'patient', 'date',), 
            )}),
        (txt('Treatment'),
            {'fields': (('treatment_type', 'area', 'parameters'),
            )}),
        (txt('Additionals'),
            {'fields': (('additional_notes'),
            )}),
            )
    list_display = ('patient', 'date')

admin.site.register(PhysiotherapyCard, PhysiotherapyCardCardAdmin)
admin.site.register(TreatmentType, FeatureCardAdmin)
admin.site.register(Area, FeatureCardAdmin)
