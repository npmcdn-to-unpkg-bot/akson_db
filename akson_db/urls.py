from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
   #     'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
