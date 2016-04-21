from common.admin import AksonCardAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import txt
from therapy_program.models import *


class NeurorehabilitationAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('orderer', 'patient', 'date',),
         )}),
        (txt('Recommendations'),
         {'fields': (('procedure_types', 'program_description', 'excercise_signatures'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date', 'procedure_types', 'program_description')


class MedicalConsultationAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('orderer', 'patient', 'date', 'diagnosis', ),
         )}),
        (txt('Recommendations'),
         {'fields': (('pharmacology_phytotherapy', 'commissioned_study'),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date', 'pharmacology_phytotherapy', 'commissioned_study')



class PhysiotherapyAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('orderer', 'patient', 'date',),
         )}),
        (txt('Recommendations'),
         {'fields': (('treatment_type', 'area', 'parameters', 'quantity',),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date', 'parameters', 'quantity')


class MassageReflexologyAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('orderer', 'patient', 'date',),
         )}),
        (txt('Recommendations'),
         {'fields': (('treatment_type', 'area', 'quantity',),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date', 'quantity')


class DietAdmin(AksonCardAdmin):
    fieldsets = (
        (txt('General'),
         {'fields': (
             ('orderer', 'patient', 'date',),
         )}),
        (txt('Recommendations'),
         {'fields': (('recommendations',),
                     )}),
        (txt('Additionals'),
         {'fields': ('additional_notes',
                     )}),
    )
    list_display = ('patient', 'date', 'recommendations')

admin.site.register(Neurorehabilitation, NeurorehabilitationAdmin)
admin.site.register(MedicalConsultation, MedicalConsultationAdmin)
admin.site.register(Physiotherapy, PhysiotherapyAdmin)
admin.site.register(MassageReflexology, MassageReflexologyAdmin)
admin.site.register(Diet, DietAdmin)
