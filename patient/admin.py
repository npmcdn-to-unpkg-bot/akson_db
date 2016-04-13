from django.db import models
from copy import deepcopy
from common.admin import AksonBaseAdmin, admin
from common.localization import txt, verbose_names_inline
from patient.models import Patient
from neurorehabilitation_card.models import NeurorehabilitationCard
from neurorehabilitation_card.admin import NeurorehabilitationCardCardAdmin


class PatientInlineBase(object):
    extra = 0
    can_delete = False
    editable_fields = []
    exclude = []

    def get_queryset(self, request):
        my_model = super(PatientInlineBase, self).get_queryset(request)
        my_model = my_model.prefetch_related(*[field.name for field in self.opts.local_many_to_many])
        my_model = my_model.prefetch_related(*[field.name for field in self.opts.local_fields if isinstance(field, (models.ForeignKey, models.ManyToManyField))])
        return my_model

    def get_readonly_fields(self, request, obj=None):
            return list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))

    def has_add_permission(self, request, obj=None):
        return False


class PatientInline(PatientInlineBase, admin.TabularInline):
    pass


@verbose_names_inline
class NeurorehabilitationCardInline(PatientInline):
    model = NeurorehabilitationCard
    fieldsets = deepcopy(NeurorehabilitationCardCardAdmin.fieldsets)


class PatientCardAdmin(AksonBaseAdmin):
    model = Patient
    inlines = [
        #     TimeSpreadInline,
        #     GaitReeducationCardInline,
        #     TrackGaitTrainingInline,
        NeurorehabilitationCardInline,
        #     PhysiotherapyCardInline,
        #     MetricCardInline,
        #     UpperLimbStudyInline,
        #     UpperLimbTherapyInline,
        #     MassageReflexologyCardInline,
        #     TreatmentRecordInline,
        #            # AsiaCardInline,
    ]
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
