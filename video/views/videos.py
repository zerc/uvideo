# coding: utf-8
from django.http import JsonResponse, Http404
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import BaseDeleteView, TemplateResponseMixin

from video import models
from .base import AttiribToContextMixin, CanUpdateMixin

__ALL__ = ('VideoDetailView', 'VideoUpdateView', 'VideoDeleteView')


class VideoDetailView(AttiribToContextMixin, CanUpdateMixin, DetailView):
    template_name = 'video/video_detail.html'
    model = models.Video


class VideoUpdateView(AttiribToContextMixin, CanUpdateMixin, UpdateView):
    template_name = 'video/collection_form.html'
    model = models.Video
    fields = ('title', 'cover', 'description', 'video_file')
    context__button_title = 'Update'
    context__form_title = 'Update video information'


class VideoDeleteView(TemplateResponseMixin, CanUpdateMixin, BaseDeleteView):
    model = models.Video
    content_type = 'application/json'

    def delete(self, request, *args, **kwargs):
        super(VideoDeleteView, self).delete(request, *args, **kwargs)
        return JsonResponse({})

    def get_success_url(self):
        return None

    def get(self, *args, **kwargs):
        raise Http404
