from django.contrib import admin
from massage_reflexology_card.models import *

from common.feature import FeatureCardAdmin
from common.admin import AksonCardAdmin

from django.utils.translation import gettext_lazy as _

class MassageReflexologyCardCardAdmin(AksonCardAdmin):
    fieldsets = (
        (_('General'),
            {'fields': (
                ('therapist', 'patient', 'date',),
            )}),
        (_('Info'),
            {'fields': (('massage_reflexology_treatment', 'massage_reflexology_area'),
            )}),
        (_('Additionals'),
            {'fields': (('additional_notes'),
            )}),
            )
    list_display = ('patient', 'date',)

admin.site.register(MassageReflexologyCard, MassageReflexologyCardCardAdmin)

admin.site.register(MassageReflexologyTreatment, FeatureCardAdmin)
admin.site.register(MassageReflexologyArea, FeatureCardAdmin)
