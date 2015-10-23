from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    url(r'', include('social_auth.urls')),
    url(r'', include('video.urls', app_name='video',
        namespace='video')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
