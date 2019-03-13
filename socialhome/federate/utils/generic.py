import datetime
import logging

import django_rq
from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpRequest
from django.utils.timezone import now
from dynamic_preferences.registries import global_preferences_registry
from federation.types import RequestType

from socialhome import __version__ as version
from socialhome.content.enums import ContentType

logger = logging.getLogger("socialhome")


def get_nodeinfo2_data():
    """
    Return data set for a NodeInfo2 document.
    """
    from socialhome.content.models import Content  # Circulars
    from socialhome.users.models import User  # Circulars
    site = Site.objects.get_current()
    data = {
        "server": {
            "baseUrl": settings.SOCIALHOME_URL,
            "name": site.name,
            "software": "socialhome",
            "version": version,
        },
        "relay": settings.SOCIALHOME_RELAY_SCOPE,
        "openRegistrations": settings.ACCOUNT_ALLOW_REGISTRATION,
    }
    if settings.SOCIALHOME_STATISTICS:
        data.update({"usage": {
            "users": {
                "total": User.objects.count(),
                "activeHalfyear": User.objects.filter(last_login__gte=now() - datetime.timedelta(days=180)).count(),
                "activeMonth": User.objects.filter(last_login__gte=now() - datetime.timedelta(days=30)).count(),
                "activeWeek": User.objects.filter(last_login__gte=now() - datetime.timedelta(days=7)).count(),
            },
            "localPosts": Content.objects.filter(author__user__isnull=False, content_type=ContentType.CONTENT).count(),
            "localComments": Content.objects.filter(author__user__isnull=False, content_type=ContentType.REPLY).count(),
        }})
    if settings.SOCIALHOME_SHOW_ADMINS:
        data.update({"organization": {
            "contact": settings.ADMINS[0][1],
            "name": settings.ADMINS[0][0],
        }})
    return data


def queue_payload(request: HttpRequest, uuid: str = None):
    """
    Queue payload for processing.
    """
    from socialhome.federate.tasks import receive_task  # Circulars
    try:
        # Create a simpler request object we can push to RQ
        headers = {k.replace('HTTP_', '').lower().replace('_', '-').capitalize(): v for k, v in request.META.items()}
        _request = RequestType(
            body=request.body,
            headers=headers,
            method=request.method,
            url=request.build_absolute_uri(),
        )
        preferences = global_preferences_registry.manager()
        if preferences["admin__log_all_receive_payloads"]:
            logger.debug("queue_payload - Request: %s", _request)
        django_rq.enqueue(receive_task, _request, uuid=uuid)
        return True
    except Exception:
        logger.exception('Failed to enqueue payload')
        return False
