from common.models import *
from common.localization import _, verbose_names


@verbose_names
class Patient(models.Model):
    # private
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    GENDER = (
        (_('M'), _('male')),
        (_('F'), _('female'))
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    BLOOD_TYPE = (
        (_('0Rh-'), _('0Rh-')),
        (_('0Rh+'), _('0Rh+')),
        (_('ARh-'), _('ARh-')),
        (_('ARh+'), _('ARh+')),
        (_('BRh-'), _('BRh-')),
        (_('BRh+'), _('BRh+')),
        (_('ABR-'), _('ABRh-')),
        (_('ABR+'), _('ABRh+')),
    )
    blood_type = models.CharField(max_length=4, choices=BLOOD_TYPE, blank=True, null=True)
    birth_date = models.DateField()
    pesel = PESELField()

    # address
    country = models.CharField(max_length=80, default="Polska")
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=80, blank=True, null=True)

    # mailing_address
    mailing_country = models.CharField(max_length=80, blank=True, null=True)
    mailing_city = models.CharField(max_length=80, blank=True, null=True)
    mailing_address = models.CharField(max_length=80, blank=True, null=True)

    # work
    job = models.CharField(max_length=80, blank=True, null=True)
    workplace = models.CharField(max_length=80, blank=True, null=True)

    # contact
    cell_phone = models.CharField(max_length=80, blank=True, null=True)
    landline_phone = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # injury info
    date_of_injury = models.DateField()
    time_of_injury = models.TimeField(blank=True, null=True)
    date_of_operation = models.DateField(blank=True, null=True)
    time_of_operation = models.TimeField(blank=True, null=True)
    therapy_program = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')
