from django.contrib import admin
from gait_reeducation_card.models import *

from common.feature import FeatureCardAdmin
from common.admin import AksonCardAdmin

from django.utils.translation import gettext_lazy as _

class GaitReeducationCardCardAdmin(AksonCardAdmin):
    fieldsets = (
        (_('General'),
            {'fields': (
                ('leading_people', 'patient', 'date',),
            )}),
        (_('Helpers'),
            {'fields': (('tool', 'left_orthosis', 'right_orthosis'),
            )}),
        (_('Environment'),
            {'fields': (('distance', 'gait_time', 'vertical_load', 'horizontal_load'),
                ('assurance_type', 'displacement_type'),
            )}),
        (_('Results'),
            {'fields': (('accented_traits', 'gait_coefficients', 'akson_gait_index'),
            )}),
        (_('Additionals'),
            {'fields': (('additional_notes'),
            )}),
            )
    list_display = ('patient', 'date', 'distance', 'gait_time')
    labels = ('leading_people', 'date', 'tool', 'left_orthosis', 'right_orthosis', 'distance', 'gait_time', 'tool', 'akson_gait_index')

admin.site.register(GaitReeducationCard, GaitReeducationCardCardAdmin)

admin.site.register(ReeducationTool, FeatureCardAdmin)
admin.site.register(OrthosisType, FeatureCardAdmin)
admin.site.register(AccentedTrait, FeatureCardAdmin)
admin.site.register(GaitCoefficient, FeatureCardAdmin)
admin.site.register(AksonGaitIndex, FeatureCardAdmin)
admin.site.register(AssuranceType, FeatureCardAdmin)
admin.site.register(DisplacementType, FeatureCardAdmin)
