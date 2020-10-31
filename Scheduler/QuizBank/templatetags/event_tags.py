from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def is_integer(target):
    try:
        int(target)
        return True
    except:
        return False

@register.filter
def turn_integer(target):
    try:
        x = int(float(target))
        return x
    except:
        return False

@register.filter
def insert_br(content):
    content = str(content).split('<br>')
    content = '<br>'.join(content)
    return mark_safe(content)
