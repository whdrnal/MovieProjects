from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def sum(obj):
    result = len(obj)
    return mark_safe(result)
