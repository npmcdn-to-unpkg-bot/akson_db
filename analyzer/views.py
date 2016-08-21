from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse

from patient.models import Patient


def check_superuser(user):
    return user.is_superuser


@login_required(login_url='/login/')
@user_passes_test(check_superuser)
def index(request):
    return render(request, 'analyzer/index.html')


@login_required(login_url='/login/')
@user_passes_test(check_superuser)
def get_patients(request):
    return JsonResponse({'patients': list(Patient.objects.values_list('id', 'first_name', 'last_name'))})
