from common.models import *
from common.feature import Feature
from common.localization import verbose_names


@verbose_names
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    groups = models.ManyToManyField('Group')

    pesel = PESELField()
    employment_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    title = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


@verbose_names
class Group(Feature):
    pass
