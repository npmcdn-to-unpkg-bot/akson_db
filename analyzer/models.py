from common.models import *
from common.localization import verbose_names
from patient.models import Patient
from datetime import datetime


@verbose_names
class NeurorehabilitationChart(models.Model):
    patient = models.ForeignKey(Patient)
    name = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now, blank=True, null=True)
    excercise_signatures = models.ManyToManyField('neurorehabilitation_card.ExcerciseSignature')

    additional_notes = AdditionalNotesField(blank=True, null=True)

    class Meta:
        ordering = ('patient', 'start_date',)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.patient, self.name, self.start_date, self.end_date)
