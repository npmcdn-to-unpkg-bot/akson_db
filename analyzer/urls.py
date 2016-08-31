from . import views
from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'patient', views.PatientViewSet)
router.register(r'excercise_signature', views.SignatureViewSet)
router.register(r'neurorehabilitation_chart', views.NeurorehabilitationCardsViewSet)
router.register(r'neurorehabilitation_data', views.NeurorehabilitationDataViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/neurorehabilitation_data/fields', views.neurorehabilitation_fields, name='neurorehabilitation_fields'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
