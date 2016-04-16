from django import template
from django.utils.translation import gettext_lazy as txt

register = template.Library()


def get_left_right_measure(value):
    val = str(value)
    if '_right_' in val:
        return txt(val.split('_right_')[-1])
    elif '_left_' in val:
        return txt(val.split('_left_')[-1])
    else:
        return txt(val.split('_right')[0].split('_left')[0])

register.filter('get_left_right_measure', get_left_right_measure)
