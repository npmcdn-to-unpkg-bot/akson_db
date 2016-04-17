from common.models import *
from common.feature import Feature
from common.localization import verbose_names
from patient.models import Patient

from django.contrib.auth.models import User
import os


def get_upload_path(instance, filename):
    dir_name = "patient_%d" % instance.patient.id
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return os.path.join(dir_name, filename)


@verbose_names
class TreatmentRecord(models.Model):
    # private
    patient = models.ForeignKey(Patient)
    leading_people = models.ManyToManyField(User)
    treatment_date = models.DateField()
    category = models.ManyToManyField('Category')
    description = DescriptionField(blank=True, null=True)
    document = models.FileField(upload_to=get_upload_path, blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.patient, self.treatment_date)

    class Meta:
        ordering = ('patient', 'treatment_date',)


@verbose_names
class Category(Feature):
    pass
