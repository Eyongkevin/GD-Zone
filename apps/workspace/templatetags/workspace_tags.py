import math
from django import template

register = template.Library()


@register.filter(name="round_up")
def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier
