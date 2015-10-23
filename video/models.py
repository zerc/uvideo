# coding: utf-8
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property

from pyuploadcare.dj import FileField, ImageField
from pyuploadcare.api_resources import File


@python_2_unicode_compatible
class AbstractContentModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover = ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ('-created',)


class Collection(AbstractContentModel):
    """ Collection of videos
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def get_absolute_url(self):
        return reverse('video:collection-detail', args=(self.pk,))


class Video(AbstractContentModel):
    """ One video
    """
    collection = models.ForeignKey(Collection)
    order = models.IntegerField(default=0, db_index=True)
    video_file = FileField()

    class Meta:
        ordering = ('order', '-created', '-id')

    def get_absolute_url(self):
        return reverse('video:video-detail', args=(self.pk,))

    @cached_property
    def user(self):
        return self.collection.user
