from common.admin import AksonBaseAdmin, admin
from common.localization import _
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
        (_('Private'),
         {'fields': (
             ('first_name', 'last_name'),
             ('gender', 'blood_type'),
             ('pesel', 'birth_date'),
         )}),
        (_('Address data'),
         {'fields': (('country', 'city', 'address'),
                     )}),
        (_('Mailing address'),
         {'fields': (('mailing_country', 'mailing_city', 'mailing_address'),
                     )}),
        (_('Work'),
         {'fields': (('job', 'workplace'),
                     )}),
        (_('Contact'),
         {'fields': (('cell_phone', 'landline_phone', 'email'),
                     )}),
        (_('Injury info'),
         {'fields': (('date_of_injury', 'time_of_injury',),
                     ('date_of_operation', 'time_of_operation',),
                     ('therapy_program',)
                     )})
    )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['sides'] = ['left', 'right']
        extra_context['joint_measures'] = ['active_motion', 'passive_motion', 'muscle_strength']
        extra_context['sftr_header'] = ['joints', 'plane_symbol', 'movements']
        return super(PatientCardAdmin, self).change_view(request, object_id=object_id, form_url=form_url,
                                                         extra_context=extra_context)

    list_display = ('last_name', 'first_name', 'birth_date', 'date_of_injury')
    search_fields = ['last_name', 'first_name']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Patient, PatientCardAdmin)
