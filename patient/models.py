from common.models import *
from common.localization import _, verbose_names


@verbose_names
class Patient(models.Model):
    # private
    first_name = models.CharField(max_length=30)
    _('first_name')
    last_name = models.CharField(max_length=50)
    _('last_name')

    GENDER = (
        (_('M'), _('male')),
        (_('F'), _('female'))
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    _('gender')

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
    blood_type = models.CharField(max_length=4, choices=BLOOD_TYPE, blank = True, null = True)
    _('blood_type')

    birth_date = models.DateField()
    _('birth_date')
    pesel = PESELField()
    _('pesel')

    # address
    country = models.CharField(max_length=40, default="Polska")
    _('country')
    city = models.CharField(max_length=40)
    _('city')
    address  = models.CharField(max_length=40, blank = True, null = True)
    _('address')

    # mailing_address
    mailing_country = models.CharField(max_length=40, blank = True, null = True)
    _('mailing_country')
    mailing_city = models.CharField(max_length=40, blank = True, null = True)
    _('mailing_city')
    mailing_address  = models.CharField(max_length=40, blank = True, null = True)
    _('mailing_address')

    # work
    job = models.CharField(max_length=20, blank = True, null = True)
    _('job')
    workplace = models.CharField(max_length=50, blank = True, null = True)
    _('workplace')

    # contact
    cell_phone = models.CharField(max_length=30, blank = True, null = True)
    _('cell_phone')
    landline_phone = models.CharField(max_length=30, blank = True, null = True)
    _('landline_phone')
    email = models.EmailField(blank = True, null = True)
    _('email')

    # injury info
    date_of_injury = models.DateField()
    _('date_of_injury')
    time_of_injury = models.TimeField(blank = True, null = True)
    _('time_of_injury')
    date_of_operation = models.DateField(blank = True, null = True)
    _('date_of_operation')
    time_of_operation = models.TimeField(blank = True, null = True)
    _('time_of_operation')
    therapy_program = models.TextField(blank = True, null = True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')

_('patient')
_('patients')
