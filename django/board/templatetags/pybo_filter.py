from django import template

register = template.Library()

@register.filter # 역순 필터
def sub(value, arg):
    return value - arg