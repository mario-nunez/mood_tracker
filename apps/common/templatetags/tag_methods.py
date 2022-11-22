from django import template


register = template.Library()


@register.filter()
def to_float(value):
    return float(value)


@register.filter()
def get_decimals(value):
    return float(value) % 1
