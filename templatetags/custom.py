from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

def path_list(url:str)->list:
    url = str(url)
    broken_url = url.strip()
    broken_url = broken_url.split("/")
    return broken_url

@register.filter
@stringfilter
def last_url(value:str,place=-1):
    if value.endswith("/"):
        value = value[:-1]
    if value.startswith("/"):
        value = value[1:]
    value = path_list(value)
    value = value[place]
    return value

@register.filter
@stringfilter
def url_section(value:str,until=1)->str:
    url_parts = path_list(value)
    url_selected = url_parts[:until]
    url_section = "/"
    for v in url_selected:
        part = f"{v}/"
        url_section += part
    return url_section


@register.inclusion_tag("tags/breadcrumb.html")
def breadcrumb(url:str):
    path_list_local = path_list(url)
    list_length = len(path_list_local)+1
    url_list = []
    for i in range(0,list_length):
        section = url_section(url,i)
        url_list.append(section)
    return {"url_list":url_list[1:]}


