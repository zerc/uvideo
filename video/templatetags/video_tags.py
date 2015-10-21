# coding: utf-8
from django import template
from django.conf import settings
from funcy import ichunks

from video.models import Collection

register = template.Library()


@register.inclusion_tag('video/tags/recent_collections_block.html')
def render_recent_collections_block(limit=10):
    """ Renders last block with last collections for index page.
    """
    qs = Collection.objects.all().order_by('-id')[:limit]
    videos_chunks = ichunks(2, qs)
    return locals()
