from . import views
from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'patient', views.PatientViewSet)
router.register(r'signature', views.SignatureViewSet)
router.register(r'neurorehabilitation_chart', views.NeurorehabilitationChartViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
