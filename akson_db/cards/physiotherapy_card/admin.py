from django.contrib import admin
from physiotherapy_card.models import *

from common.feature import FeatureCardAdmin
from common.admin import AksonCardAdmin

from django.utils.translation import gettext_lazy as _

class PhysiotherapyCardCardAdmin(AksonCardAdmin):
    fieldsets = (
        (_('General'), 
            {'fields': (
                ('leading_people', 'patient', 'date',), 
            )}),
        (_('Treatment'),
            {'fields': (('treatment_type', 'area', 'parameters'),
            )}),
        (_('Additionals'),
            {'fields': (('additional_notes'),
            )}),
            )
    list_display = ('patient', 'date')

admin.site.register(PhysiotherapyCard, PhysiotherapyCardCardAdmin)

admin.site.register(TreatmentType, FeatureCardAdmin)
admin.site.register(Area, FeatureCardAdmin)
