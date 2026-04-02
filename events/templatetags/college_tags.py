from django import template
from events.models import College

register = template.Library()

@register.simple_tag
def get_college_logo(college_name):
    """College name se logo URL return karo, nahi mila to None"""
    try:
        college = College.objects.get(name__iexact=college_name)
        if college.logo:
            return college.logo.url
    except College.DoesNotExist:
        pass
    return None
