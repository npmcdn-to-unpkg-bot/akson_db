from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings

import json

from neurorehabilitation_card.models import NeurorehabilitationCard


def users(request):
    users = User.objects.order_by('-username').values_list('id', 'first_name', 'last_name')
    return JsonResponse({'users': list(users)})


def user_months(request):
    user_id = 10
    User.objects.get(id__exact=user_id)
    return JsonResponse({'users': [model_to_dict(user) for user in users]})


#def get_user_months(resp):



def index(request):
    users = User.objects.order_by('-get_full_name')
    context = {'users': users}
    return render(request, 'supervision/index.html', context)
