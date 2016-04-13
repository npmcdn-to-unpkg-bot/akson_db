from django.contrib.admin.models import LogEntry
from common.admin import AksonBaseAdmin, admin
from common.feature import FeatureCardAdmin
from common.localization import _
from person.models import Person, Group


class PersonAdmin(AksonBaseAdmin):
    fieldsets = (
        (_('Basic info'),
            {'fields': (
                ('first_name', 'last_name', 'groups'),
                )}),
        (_('Additionals'),
            {'fields': (
                ('pesel', 'address', 'employment_date', 'title', 'education', 'specialization'),
                )}),
        )

    def get_groups(self, obj):
        return ", ".join([p.name for p in obj.groups.all()])
    get_groups.short_description = _("groups")

    list_display = ('last_name', 'first_name', 'get_groups')


class GroupAdmin(FeatureCardAdmin):
    def get_persons(self, obj):
        return ", ".join([p.last_name for p in obj.person_set.all()])
    get_persons.short_description = _("persons")

    list_display = ('name', 'description', 'get_persons')

admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(LogEntry)
