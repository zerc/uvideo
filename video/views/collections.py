# coding: utf-8
from funcy import silent

from django.db import transaction
from django.http import JsonResponse, Http404
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from video import forms, models
from .base import AttiribToContextMixin, CanUpdateMixin, AddUserToKwargs

__ALL__ = ('CollectionCreateView', 'CollectionListView',
           'CollectionDetailView', 'CollectionDetailView')


class CollectionCreateView(AttiribToContextMixin, AddUserToKwargs, CreateView):
    template_name = 'video/collection_form.html'
    form_class = forms.CollectionForm
    context__button_title = 'Add new collection'
    context__form_title = 'Add new collection'


class CollectionListView(AttiribToContextMixin, ListView):
    model = models.Collection
    template_name = 'video/colleciton_list.html'
    paginate_by = 20


class CollectionDetailView(AttiribToContextMixin, CanUpdateMixin, DetailView):
    template_name = 'video/collection_detail.html'
    model = models.Collection


class CollectionUpdateView(AttiribToContextMixin, AddUserToKwargs,
                           CanUpdateMixin, UpdateView):
    template_name = 'video/collection_form.html'
    form_class = forms.CollectionForm
    model = models.Collection
    context__button_title = 'Update'
    context__form_title = 'Update collection'


class CollectionUpdateVideoPos(CanUpdateMixin, UpdateView):
    model = models.Collection
    content_type = 'application/json'

    def post(self, *args, **kwargs):
        new_orders = self.request.POST.copy()
        result = JsonResponse({})

        if not new_orders:
            return result

        obj = self.get_object()

        with transaction.atomic():
            for video in obj.video_set.all():
                video.order = new_orders.get(str(video.pk))
                if video.order is not None:
                    video.save()

        return result

    def get_success_url(self):
        return None

    def get(self, *args, **kwargs):
        raise Http404
