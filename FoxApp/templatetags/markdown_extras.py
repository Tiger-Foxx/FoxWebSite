# templatetags/markdown_extras.py
from django import template
from django.template.defaultfilters import stringfilter
from markdown_deux import markdown as md2

register = template.Library()

@register.filter
@stringfilter
def md(value):
    return md2(value)