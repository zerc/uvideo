# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^add/$', views.CollectionCreateView.as_view(),
        name='collection-add'),

    url(r'^(?P<pk>\d+)/$', views.CollectionDetailView.as_view(),
        name='collection-detail'),

    url(r'^(?P<pk>\d+)/update$', views.CollectionUpdateView.as_view(),
        name='collection-update'),

    url(r'^video/(?P<pk>\d+)/$', views.VideoDetailView.as_view(),
        name='video-detail'),

    url(r'^video/(?P<pk>\d+)/update$', views.VideoUpdateView.as_view(),
        name='video-update'),

    url(r'^video/(?P<pk>\d+)/delete$', views.VideoDeleteView.as_view(),
        name='video-delete')
)
