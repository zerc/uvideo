# coding: utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^$', views.CollectionListView.as_view(),
        name='collection-list'),

    url(r'^add/$', login_required(views.CollectionCreateView.as_view()),
        name='collection-add'),

    url(r'^(?P<pk>\d+)/update$',
        login_required(views.CollectionUpdateView.as_view()),
        name='collection-update'),

    url(r'^(?P<pk>\d+)/update-video-order$',
        login_required(views.CollectionUpdateVideoPos.as_view()),
        name='collection-update-video-order'),

    url(r'^(?P<pk>\d+)/$', views.CollectionDetailView.as_view(),
        name='collection-detail'),

    url(r'^video/(?P<pk>\d+)/$', views.VideoDetailView.as_view(),
        name='video-detail'),

    url(r'^video/(?P<pk>\d+)/update$',
        login_required(views.VideoUpdateView.as_view()),
        name='video-update'),

    url(r'^video/(?P<pk>\d+)/delete$',
        login_required(views.VideoDeleteView.as_view()),
        name='video-delete'),
)
