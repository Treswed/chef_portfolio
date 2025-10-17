from .models import Statistic


def site_stats(request):
    """Inject ordered statistics into templates as `site_stats`.

    Returns a list of dicts: [{'key':..., 'label':..., 'value':..., 'icon':...}, ...]
    """
    stats = []
    try:
        stats_qs = Statistic.objects.all()
        for s in stats_qs:
            stats.append({'key': s.key, 'label': s.label, 'value': s.value, 'icon': s.icon})
    except Exception:
        # If migrations haven't been run yet, fail gracefully in templates
        pass
    return {'site_stats': stats}
