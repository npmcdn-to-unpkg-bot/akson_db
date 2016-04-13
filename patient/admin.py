from common.admin import AksonBaseAdmin, admin
from common.localization import txt
from patient.models import Patient


class PatientCardAdmin(AksonBaseAdmin):
    model = Patient
    # inlines = [
    #     TimeSpreadInline,
    #     GaitReeducationCardInline,
    #     TrackGaitTrainingInline,
    #     NeurorehabilitationCardInline,
    #     PhysiotherapyCardInline,
    #     MetricCardInline,
    #     UpperLimbStudyInline,
    #     UpperLimbTherapyInline,
    #     MassageReflexologyCardInline,
    #     TreatmentRecordInline,
    #            # AsiaCardInline,
    # ]
    fieldsets = (
        (txt('Private'),
         {'fields': (
             ('first_name', 'last_name'),
             ('gender', 'blood_type'),
             ('pesel', 'birth_date'),
         )}),
        (txt('Address data'),
         {'fields': (('country', 'city', 'address'),
                     )}),
        (txt('Mailing address'),
         {'fields': (('mailing_country', 'mailing_city', 'mailing_address'),
                     )}),
        (txt('Work'),
         {'fields': (('job', 'workplace'),
                     )}),
        (txt('Contact'),
         {'fields': (('cell_phone', 'landline_phone', 'email'),
                     )}),
        (txt('Injury info'),
         {'fields': (('date_of_injury', 'time_of_injury',),
                     ('date_of_operation', 'time_of_operation',),
                     ('therapy_program',)
                     )})
    )

    list_display = ('last_name', 'first_name', 'birth_date', 'date_of_injury')
    search_fields = ['last_name', 'first_name']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Patient, PatientCardAdmin)
