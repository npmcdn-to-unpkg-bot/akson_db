from django.db import models
from copy import deepcopy
from common.admin import AksonBaseAdmin, admin
from common.localization import txt, verbose_names_inline
from patient.models import Patient
from gait_reeducation_card.admin import GaitReeducationCard, GaitReeducationCardCardAdmin
from massage_reflexology_card.admin import MassageReflexologyCard, MassageReflexologyCardCardAdmin
from metric_card.admin import MetricCard, MetricCardCardAdmin
from neurorehabilitation_card.admin import NeurorehabilitationCard, NeurorehabilitationCardCardAdmin
from physiotherapy_card.admin import PhysiotherapyCard, PhysiotherapyCardCardAdmin
from time_spread.admin import TimeSpread, TimeSpreadCardAdmin
from track_gait_training.admin import TrackGaitTraining, TrackGaitTrainingCardAdmin
from treatment_record.admin import TreatmentRecord, TreatmentRecordCardAdmin
from upper_limb_study.admin import UpperLimbStudy, UpperLimbStudyCardAdmin
from upper_limb_therapy.admin import UpperLimbTherapy, UpperLimbTherapyCardAdmin


class PatientInlineBase(object):
    extra = 0
    can_delete = False
    editable_fields = []
    exclude = []

    def get_queryset(self, request):
        my_model = super(PatientInlineBase, self).get_queryset(request)
        my_model = my_model.prefetch_related(*[field.name for field in self.opts.local_many_to_many])
        my_model = my_model.prefetch_related(*[field.name for field in self.opts.local_fields if
                                               isinstance(field, (models.ForeignKey, models.ManyToManyField))])
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


class PatientStackedInline(PatientInlineBase, admin.StackedInline):
    pass


@verbose_names_inline
class GaitReeducationCardInline(PatientInline):
    model = GaitReeducationCard
    fieldsets = deepcopy(GaitReeducationCardCardAdmin.fieldsets)


@verbose_names_inline
class TrackGaitTrainingInline(PatientInline):
    model = TrackGaitTraining
    fieldsets = deepcopy(TrackGaitTrainingCardAdmin.fieldsets)


@verbose_names_inline
class NeurorehabilitationCardInline(PatientInline):
    model = NeurorehabilitationCard
    fieldsets = deepcopy(NeurorehabilitationCardCardAdmin.fieldsets)


@verbose_names_inline
class PhysiotherapyCardInline(PatientInline):
    model = PhysiotherapyCard
    fieldsets = deepcopy(PhysiotherapyCardCardAdmin.fieldsets)


@verbose_names_inline
class MetricCardInline(PatientStackedInline):
    model = MetricCard
    fieldsets = deepcopy(MetricCardCardAdmin.fieldsets)


@verbose_names_inline
class TreatmentRecordInline(PatientInline):
    model = TreatmentRecord
    fieldsets = deepcopy(TreatmentRecordCardAdmin.fieldsets)


@verbose_names_inline
class TimeSpreadInline(PatientInline):
    model = TimeSpread
    fieldsets = deepcopy(TimeSpreadCardAdmin.fieldsets)


@verbose_names_inline
class UpperLimbStudyInline(PatientStackedInline):
    model = UpperLimbStudy
    fieldsets = deepcopy(UpperLimbStudyCardAdmin.fieldsets)


@verbose_names_inline
class MassageReflexologyCardInline(PatientInline):
    model = MassageReflexologyCard
    fieldsets = deepcopy(MassageReflexologyCardCardAdmin.fieldsets)


@verbose_names_inline
class UpperLimbTherapyInline(PatientInline):
    model = UpperLimbTherapy
    fieldsets = deepcopy(UpperLimbTherapyCardAdmin.fieldsets)


class PatientCardAdmin(AksonBaseAdmin):
    change_form_template = 'patient.html'
    model = Patient
    inlines = [
        TimeSpreadInline,
        GaitReeducationCardInline,
        TrackGaitTrainingInline,
        NeurorehabilitationCardInline,
        PhysiotherapyCardInline,
        MetricCardInline,
        UpperLimbStudyInline,
        UpperLimbTherapyInline,
        MassageReflexologyCardInline,
        TreatmentRecordInline,
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
                     ('additional_notes',)
                     )})
    )

    list_display = ('last_name', 'first_name', 'birth_date', 'date_of_injury')
    search_fields = ['last_name', 'first_name']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Patient, PatientCardAdmin)
