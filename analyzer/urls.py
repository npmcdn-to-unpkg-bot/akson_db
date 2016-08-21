from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patients/$', views.get_patients, name='get_patients'),
    url(r'^signatures/$', views.get_signatures, name='get_signatures'),
]
