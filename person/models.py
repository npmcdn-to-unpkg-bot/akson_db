from common.models import *
from common.feature import Feature
from common.localization import _, verbose_names


@verbose_names
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    groups = models.ManyToManyField('Group')

    pesel = PESELField()
    employment_date = models.DateField(blank = True, null = True)
    _('employment_date')
    address  = models.CharField(max_length=200, blank = True, null = True)

    title = models.CharField(max_length=20, blank = True, null = True)
    _('title')
    education = models.CharField(max_length=40, blank = True, null = True)
    _('education')
    specialization = models.CharField(max_length=200, blank = True, null = True)
    _('specialization')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

_('person')
_('persons')


@verbose_names
class Group(Feature):
    pass
_('groups')
