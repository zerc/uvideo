# coding: utf-8
from django.db import models
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

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Collection(AbstractContentModel):
    """ Collection of videos
    """
    def get_absolute_url(self):
        return reverse('video:collection-detail', args=(self.pk,))


class Video(AbstractContentModel):
    """ One video
    """
    collection = models.ForeignKey(Collection)
    video_file = FileField()

    def get_absolute_url(self):
        return reverse('video:video-detail', args=(self.pk,))
