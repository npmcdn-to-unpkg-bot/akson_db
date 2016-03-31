import re
from django.utils.translation import ugettext as _

camelcase_to_underscore = lambda str: re.sub('(((?<=[a-z])[A-Z0-9])|([A-Z0-9](?![A-Z0-9]|$)))', '_\\1', str).lower().strip('_')

def verbose_names(model):
    app_name = camelcase_to_underscore(model.__module__.split('.')[0])
    text = camelcase_to_underscore(model.__name__)
    for field in model._meta.fields:
        setattr(field, 'verbose_name', _(field.name))
    for field in model._meta.many_to_many:
        setattr(field, 'verbose_name', _(field.name))
    model._meta.app_label = string_with_title(app_name, _(app_name))
    model._meta.verbose_name = _(text)
    model._meta.verbose_name_plural = _(text + 's')
    return model

class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance
    def title(self):
        return self._title.title()
    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

import inspect

def verbose_names_inline(*args):
    def model_changer(model, field_to_remove = 'patient'):
        if (model.fieldsets):
            tuple_of_tuples = model.fieldsets[0][1]['fields']
            list_of_lists = list(list(x) for x in tuple_of_tuples)
            if field_to_remove in list_of_lists[0]:
                list_of_lists[0].remove(field_to_remove)
            model.fieldsets[0][1]['fields'] = tuple(tuple(x) for x in list_of_lists)
        text = camelcase_to_underscore(model.__name__.strip('Inline'))
        return model

    def wrappee(model, field_to_remove = 'patient'):
        return model_changer(model, field_to_remove)

    if inspect.isclass(args[0]):
        return wrappee(args[0])

    def wrappee_with_args(model):
        return model_changer(model, args[0])
    return wrappee_with_args

from django.utils.translation import gettext_lazy
from django.utils import six  # Python 3 compatibility
from django.utils.functional import lazy
from django.utils.translation import force_text

def verbose_name_app(s):
    def _verbose(s):
        return force_text(s).capitalize()
    verbose = lazy(_verbose, six.text_type)
    return verbose(gettext_lazy(s))
