from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import serializers, viewsets

from patient.models import Patient
from neurorehabilitation_card.models import ExcerciseSignature
from .models import NeurorehabilitationChart


def check_superuser(user):
    return user.is_superuser


@login_required(login_url='/login/')
@user_passes_test(check_superuser)
def index(request):
    return render(request, 'analyzer/index.html')


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name')


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class NeurorehabilitationChartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NeurorehabilitationChart


class NeurorehabilitationChartViewSet(viewsets.ModelViewSet):
    queryset = NeurorehabilitationChart.objects.all()
    serializer_class = NeurorehabilitationChartSerializer


class SignatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExcerciseSignature


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = ExcerciseSignature.objects.all()
    serializer_class = SignatureSerializer
