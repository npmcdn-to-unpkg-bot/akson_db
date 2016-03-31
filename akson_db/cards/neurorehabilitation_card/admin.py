from django.contrib import admin
from neurorehabilitation_card.models import *

from common.feature import FeatureCardAdmin
from common.admin import AksonCardAdmin

from django.utils.translation import gettext_lazy as _

class NeurorehabilitationCardCardAdmin(AksonCardAdmin):
    fieldsets = (
        (_('General'),
            {'fields': (('patient', 'leading_people', 'date', ),
            )}),
        (_('Excercise'),
            {'fields': (('excercise_signature', 'load', 'repetitions', 'sets'),
            )}),
        (_('Environment'),
            {'fields': (('starting_position', 'nature_of_load', 'motion_range'),
            )}),
        (_('Results'),
            {'fields': (('time', 'frequency'),
            )}),
        (_('Additionals'),
            {'fields': (('additional_notes'),
            )}),
            )
    list_display = ('patient', 'date', 'excercise_signature', 'load', 'repetitions', 'sets', 'time', 'frequency')

admin.site.register(NeurorehabilitationCard, NeurorehabilitationCardCardAdmin)

admin.site.register(ExcerciseSignature, FeatureCardAdmin)
admin.site.register(StartingPosition, FeatureCardAdmin)
admin.site.register(NatureOfLoad, FeatureCardAdmin)
admin.site.register(MotionRange, FeatureCardAdmin)
