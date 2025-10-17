from django.utils.deprecation import MiddlewareMixin
from .models import Visit
from django.utils import timezone
import re

_exclude_paths = [
    re.compile(r'^/static/'),
    re.compile(r'^/media/'),
    re.compile(r'^/admin/'),
]


def _should_log(path):
    for rx in _exclude_paths:
        if rx.match(path):
            return False
    return True


class VisitorMiddleware(MiddlewareMixin):
    """Log basic visit info into the Visit model.

    - Skips static/media/admin paths
    - Logs only GET requests by default to reduce noise
    """
    def process_response(self, request, response):
        try:
            path = request.path
            if not _should_log(path):
                return response

            if request.method != 'GET':
                # optional: skip non-GETs to focus on page views
                return response

            Visit.objects.create(
                path=path,
                method=request.method,
                status_code=getattr(response, 'status_code', None) or None,
                ip_address=self._get_ip(request),
                user=getattr(request, 'user', None) if getattr(request, 'user', None) and request.user.is_authenticated else None,
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:255],
                referrer=request.META.get('HTTP_REFERER', '')[:500],
                session_key=getattr(request, 'session', {}).session_key or ''
            )
        except Exception:
            # never raise from middleware; best-effort logging
            pass
        return response

    def _get_ip(self, request):
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        if xff:
            # X-Forwarded-For can be a comma-separated list; client ip is first
            return xff.split(',')[0].strip()[:45]
        return request.META.get('REMOTE_ADDR', '')[:45]
