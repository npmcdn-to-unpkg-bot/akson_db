from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import serializers, viewsets

from patient.models import Patient
from neurorehabilitation_card.models import ExcerciseSignature
from .models import NeurorehabilitationChart
from neurorehabilitation_card.models import NeurorehabilitationCard


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


class NeurorehabilitationCardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NeurorehabilitationCard
        fields = ('id', 'date', 'load')


class NeurorehabilitationCardsViewSet(viewsets.ModelViewSet):
    queryset = NeurorehabilitationCard.objects.filter(patient__id=61)
    serializer_class = NeurorehabilitationCardsSerializer


class NeurorehabilitationDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NeurorehabilitationCard
        fields = ('id', 'date', 'excercise_signature', 'load', 'repetitions', 'sets')


import datetime
class NeurorehabilitationDataViewSet(viewsets.ModelViewSet):
    queryset = NeurorehabilitationCard.objects.filter()
    serializer_class = NeurorehabilitationDataSerializer

    def get_queryset(self):
        data = self.request.GET
        patient_id = data['patient_id']
        if 'begin_date' in data: begin_date = data['begin_date']
        else: begin_date = datetime.date.today() - datetime.timedelta(days=365*3) # TODO have proper default range value
        if 'end_date' in data: end_date = data['end_date']
        else: end_date = datetime.date.today()
        print(patient_id, begin_date, end_date)
        return NeurorehabilitationCard.objects.filter(
            patient__id=patient_id,
            date__range=(begin_date, end_date),
        )

class SignatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExcerciseSignature
        fields = ('id', 'name')


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = ExcerciseSignature.objects.all()
    serializer_class = SignatureSerializer


@login_required(login_url='/login/')
@user_passes_test(check_superuser)
def neurorehabilitation_fields(request):
    return JsonResponse(
        [{
            'id':1,
            'name':'Obciazenie',
            'field_name':'load'
        },
        {
            'id':2,
            'name':'Liczba powtorzen',
            'field_name':'repetitions'
        },
           {
            'id':3,
            'name':'Liczba serii',
            'field_name':'sets'
        }
    ], safe=False)
