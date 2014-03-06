from datetime import datetime, timedelta
from django import template

register = template.Library()

@register.filter
def date_format(date):
    format = ''
    today = datetime.today()
    yesterday = today + timedelta(days=-1)
    if date.strftime("%Y-%m-%d") == today.strftime("%Y-%m-%d"):
        format = 'gaur'
    if date.strftime("%Y-%m-%d") == yesterday.strftime("%Y-%m-%d"):
        format = 'atzo'
    if format not in ('gaur','atzo'):
        format = date.strftime("%Y-%m-%d") + ' : ' + date.strftime("%H:%M")
    else:
        format += date.strftime(" : %H:%M")
    return format
