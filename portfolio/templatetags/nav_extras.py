from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, *url_names, **kwargs):
    """
    Return 'active' when request.path matches any of the given url_names.
    Usage:
      {% load nav_extras %}
      <li class="{% active 'portfolio:home' %}"><a href="{% url 'portfolio:home' %}">Home</a></li>
      <li class="{% active 'recipes:recipe_list' startswith='true' %}">...
    If a name can't be reversed it will be treated as a raw path.

    Keyword args:
      startswith: 'true' or True -> match startswith instead of exact match
    """
    request = context.get('request')
    if not request:
        return ''
    startswith = kwargs.get('startswith', False)
    # allow template to pass startswith='true'
    if isinstance(startswith, str):
        startswith = startswith.lower() in ('1', 'true', 'yes', 'y')
    current = request.path
    for name in url_names:
        try:
            path = reverse(name)
        except NoReverseMatch:
            path = name  # treat as raw path
        if startswith:
            if current.startswith(path):
                return 'active'
        else:
            if current == path:
                return 'active'
    return ''
