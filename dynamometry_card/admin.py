from common.admin import AksonCardAdmin, admin
from common.localization import txt
from dynamometry_card.models import *


class DynamometryCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (('patient', 'examiners', 'date'),
                     )}),
        (txt('Environment'),
         {'fields': (('muscle', 'study_position', 'duration'),
                     )}),
        (txt('Results'),
         {'fields': (('max', 'max_relative'),
                     ('average', 'average_relative'),
                     ('surface_area', 'relative_surface_area'),
                     ('standard_deviation',),
                     ('to_max', 'relative_to_max'),
                     ('to_zero', 'relative_to_zero'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes', ),
          }),
    )
    list_display = ('patient', 'date', 'muscle', 'duration')

admin.site.register(DynamometryCard, DynamometryCardAdmin)
