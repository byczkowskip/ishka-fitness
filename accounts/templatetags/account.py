from typing import Any

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_host_name(context: dict[str, Any]) -> str:
    request = context['request']
    return request.META.get('HTTP_HOST')
