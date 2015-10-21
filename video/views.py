# coding: utf-8
from django.http import JsonResponse, Http404
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.views.generic.edit import BaseDeleteView, TemplateResponseMixin

from video import forms, models


class AttiribToContextMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(AttiribToContextMixin, self).get_context_data(*args,
                                                                      **kwargs)
        attr_prefix = 'context__'

        for attr in dir(self):
            if attr.startswith(attr_prefix):
                context[attr.replace(attr_prefix, '')] = getattr(self, attr)

        return context


class CollectionCreateView(AttiribToContextMixin, CreateView):
    """ Create new collections of video.
    """
    template_name = 'video/collection_form.html'
    form_class = forms.CollectionForm
    context__button_title = 'Add new collection'
    context__form_title = 'Add new collection'


class CollectionDetailView(AttiribToContextMixin, DetailView):
    template_name = 'video/collection_detail.html'
    model = models.Collection


class CollectionUpdateView(AttiribToContextMixin, UpdateView):
    template_name = 'video/collection_form.html'
    form_class = forms.CollectionForm
    model = models.Collection
    context__button_title = 'Update'
    context__form_title = 'Update collection'


class VideoDetailView(AttiribToContextMixin, DetailView):
    template_name = 'video/video_detail.html'
    model = models.Video


class VideoUpdateView(AttiribToContextMixin, UpdateView):
    template_name = 'video/collection_form.html'
    model = models.Video
    fields = ('title', 'cover', 'description', 'video_file')
    context__button_title = 'Update'
    context__form_title = 'Update video information'


class VideoDeleteView(TemplateResponseMixin, BaseDeleteView):
    model = models.Video
    content_type = 'application/json'

    def delete(self, request, *args, **kwargs):
        super(VideoDeleteView, self).delete(request, *args, **kwargs)
        return JsonResponse({})

    def get_success_url(self):
        return None

    def get(self, *args, **kwargs):
        raise Http404
