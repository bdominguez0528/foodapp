from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def menu_active(request, url_name, display_text, match_exactly=False):
    """ Return `display_text` when request.path matches
    """
    url = reverse(url_name)

    if match_exactly:
        return display_text if url == request.path else ""
    else:
        return display_text if url in request.path else ""
