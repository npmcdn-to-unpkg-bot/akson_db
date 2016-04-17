from common.admin import AksonCardAdmin, admin
from common.localization import txt
from dynamometry_card.models import *


class DynamometryCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (('patient', 'examiners', 'date'),
                     )}),
        (txt('Environment'),
         {'fields': (('muscle', 'duration'),
                     )}),
        (txt('Results'),
         {'fields': (('max_dynamometer', 'max_relative_dynamometer'),
                     ('average_dynamometer', 'average_relative_dynamometer'),
                     ('dynamometer_surface_area', 'dynamometer_relative_surface_area'),
                     ('dynamometer_standard_deviation',),
                     ('dynamometer_to_max', 'dynamometer_relative_to_max'),
                     ('dynamometer_to_zero', 'dynamometer_relative_to_zero'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes', ),
          }),
    )
    list_display = ('patient', 'date', 'muscle', 'duration')

admin.site.register(DynamometryCard, DynamometryCardAdmin)
