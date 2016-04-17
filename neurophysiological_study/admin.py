from common.admin import AksonCardAdmin, admin
from common.localization import txt
from neurophysiological_study.models import *


class NeurophysiologicalStudyAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (('patient', 'examiners', 'date', 'mass'),
                     )}),
        (txt('Results'),
         {'fields': (('MVIC', 'relative_MVIC'),
                     ('max_EMG', 'max_relative_EMG'),
                     ('average_EMG', 'average_relative_EMG'),
                     ('EMG_surface_area', 'EMG_relative_surface_area'),
                     ('EMG_standard_deviation',),
                     ('WNM',),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes', ),
          }),
    )
    list_display = ('patient', 'date', 'mass', 'WNM')

admin.site.register(NeurophysiologicalStudy, NeurophysiologicalStudyAdmin)
