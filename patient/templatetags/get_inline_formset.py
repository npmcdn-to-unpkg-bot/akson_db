from django import template

register = template.Library()


def get_inline_formset(value, verbose_name):
    return next(inline.formset.prefix for inline in value if inline.opts.verbose_name == verbose_name)


register.filter('get_inline_formset', get_inline_formset)
