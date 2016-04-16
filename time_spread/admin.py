from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from time_spread.models import *


class TimeSpreadCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('Time spreads'),
            {'fields': (('leading_doctors', 'patient',),
                        ('begin', 'end',),
            )}),
        (txt('Coefficients'),
            {'fields': (('asia', 'icd10', 'ashworth'),
            )}),
        (txt('Diagnosis'),
            {'fields': (('diagnosis',),
                        ('contraindicators',),
                        ('levels_of_injury',),
                        ('injury_unit',),
            )}),
        (txt('Treatment'),
            {'fields': (('date_of_agreement', 'rehabilitation_at_home'),
            )})
        )
    list_display = ('patient', 'begin', 'end')

admin.site.register(TimeSpread, TimeSpreadCardAdmin)
admin.site.register(ASIA, FeatureCardAdmin)
admin.site.register(ICD10, FeatureCardAdmin)
admin.site.register(Ashworth, FeatureCardAdmin)
admin.site.register(LevelOfInjury, FeatureCardAdmin)
