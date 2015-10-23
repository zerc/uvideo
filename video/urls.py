# coding: utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import user_passes_test

from utils import user_can_add_content
from . import views

decor = user_passes_test(user_can_add_content)


urlpatterns = (
    url(r'^$', views.CollectionListView.as_view(),
        name='collection-list'),

    url(r'^add/$', decor(views.CollectionCreateView.as_view()),
        name='collection-add'),

    url(r'^(?P<pk>\d+)/update$',
        decor(views.CollectionUpdateView.as_view()),
        name='collection-update'),

    url(r'^(?P<pk>\d+)/update-video-order$',
        decor(views.CollectionUpdateVideoPos.as_view()),
        name='collection-update-video-order'),

    url(r'^(?P<pk>\d+)/$', views.CollectionDetailView.as_view(),
        name='collection-detail'),

    url(r'^video/(?P<pk>\d+)/$', views.VideoDetailView.as_view(),
        name='video-detail'),

    url(r'^video/(?P<pk>\d+)/update$',
        decor(views.VideoUpdateView.as_view()),
        name='video-update'),

    url(r'^video/(?P<pk>\d+)/delete$',
        decor(views.VideoDeleteView.as_view()),
        name='video-delete'),
)
