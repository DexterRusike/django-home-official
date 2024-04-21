# Create a file called custom_tags.py inside your Django app directory
from django import template

register = template.Library()

@register.filter
def create_range(value):
    return range(value)