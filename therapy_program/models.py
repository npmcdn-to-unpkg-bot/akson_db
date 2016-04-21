from common.models import *
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
from datetime import datetime


@verbose_names
class Neurorehabilitation(models.Model):
    patient = models.ForeignKey(Patient)
    orderer = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    procedure_types = DescriptionField(blank=True, null=True)
    program_description = DescriptionField(blank=True, null=True)
    excercise_signatures = models.ManyToManyField('neurorehabilitation_card.ExcerciseSignature',
                                                  related_name="signatures", blank=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)  # TODO include in generic model

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class MedicalConsultation(models.Model):
    patient = models.ForeignKey(Patient)
    orderer = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    diagnosis = DescriptionField(blank=True, null=True)
    pharmacology_phytotherapy = DescriptionField(blank=True, null=True)
    commissioned_study = DescriptionField(blank=True, null=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)  # TODO include in generic model

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class Physiotherapy(models.Model):
    patient = models.ForeignKey(Patient)
    orderer = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    treatment_type = models.ManyToManyField('physiotherapy_card.TreatmentType', related_name="treatment_types", blank=True)
    area = models.ManyToManyField('physiotherapy_card.Area', related_name="areas", blank=True)
    parameters = DescriptionField(blank=True, null=True)
    quantity = DescriptionField(blank=True, null=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)  # TODO include in generic model

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class MassageReflexology(models.Model):
    patient = models.ForeignKey(Patient)
    orderer = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    treatment_type = models.ManyToManyField('massage_reflexology_card.MassageReflexologyTreatment',
                                            related_name="treatment_types", blank=True)
    area = models.ManyToManyField('massage_reflexology_card.MassageReflexologyArea', related_name="areas", blank=True)
    quantity = DescriptionField(blank=True, null=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)  # TODO include in generic model

    class Meta:
        ordering = ('patient', 'date',)


@verbose_names
class Diet(models.Model):
    patient = models.ForeignKey(Patient)
    orderer = models.ManyToManyField(User)
    date = models.DateField(default=datetime.now)

    recommendations = DescriptionField(blank=True, null=True)

    additional_notes = AdditionalNotesField(blank=True, null=True)  # TODO include in generic model

    class Meta:
        ordering = ('patient', 'date',)
