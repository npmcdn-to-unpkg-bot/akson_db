from django import template
from django.utils.translation import gettext_lazy as txt
import re

register = template.Library()


def get_limb_measure(value):
    val = str(value)
    return txt(val.split('_')[0] + val.split('limb')[-1])


def get_joint_measure(value):
    val = str(value)
    return txt(val.split('joint_')[-1])


def get_sftr_plane(value):
    val = str(value)
    val = val.split('_')[1]
    founded_digits = re.search("\d", val)
    if founded_digits:
        start = founded_digits.start() - 1
        return val[:start] + '(' + val[start:] + ')'
    else:
        return val


def get_sftr_movement(value):
    val = str(value)
    return txt(val.split('_sftr_')[1])

register.filter('get_limb_measure', get_limb_measure)
register.filter('get_joint_measure', get_joint_measure)
register.filter('get_sftr_plane', get_sftr_plane)
register.filter('get_sftr_movement', get_sftr_movement)
