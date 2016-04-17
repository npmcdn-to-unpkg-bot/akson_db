from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from treatment_record.models import *


class TreatmentRecordCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('leading_people', 'patient', 'treatment_date',),
         )}),
        (txt('Info'),
         {'fields': (('category', 'description',),
                     ('document',)
                     )}),
    )
    list_display = ('patient', 'treatment_date')

    class Media:
        from django.conf import settings
        static_url = getattr(settings, 'STATIC_URL', '/static/')


admin.site.register(TreatmentRecord, TreatmentRecordCardAdmin)
admin.site.register(Category, FeatureCardAdmin)
