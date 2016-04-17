from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from neurorehabilitation_card.models import *


class NeurorehabilitationCardAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (('patient', 'leading_people', 'date',),
                     )}),
        (txt('Excercise'),
         {'fields': (('excercise_signature', 'load', 'repetitions', 'sets'),
                     )}),
        (txt('Environment'),
         {'fields': (('starting_position', 'nature_of_load', 'motion_range'),
                     )}),
        (txt('Results'),
         {'fields': (('time', 'frequency'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes', ),
          }),
    )
    list_display = ('patient', 'date', 'excercise_signature', 'load', 'repetitions', 'sets', 'time', 'frequency')


admin.site.register(NeurorehabilitationCard, NeurorehabilitationCardAdmin)

admin.site.register(ExcerciseSignature, FeatureCardAdmin)
admin.site.register(StartingPosition, FeatureCardAdmin)
admin.site.register(NatureOfLoad, FeatureCardAdmin)
admin.site.register(MotionRange, FeatureCardAdmin)
