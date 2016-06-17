from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users$', views.users, name='get_users'),
    url(r'^user_months$', views.user_months, name='get_user_months'),
]
