from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse

from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_users():
    raw_users = list(User.objects.values_list('id', 'first_name', 'last_name'))
    users = [{'id': raw_user[0], 'full_name': "{0} {1}".format(*raw_user[1:])} for raw_user in raw_users]
    return {'users': sorted(list(users), key=lambda user: user['full_name'])}


def get_queryset(user, app, start_date):
    qs_name = app.replace('_', '') + '_set'
    return getattr(user, qs_name).filter(date__year=start_date.year, date__month=start_date.month)


def get_summary_data(user_id):
    relative_month = 12

    user = User.objects.get(id__exact=user_id)
    data = [list(map(_, ['month'] + settings.SUPERVISED_APPS))]
    unique_patients = [list(map(_, ['month'] + settings.SUPERVISED_APPS))]

    for month in range(relative_month):
        start_date = datetime.now() - relativedelta(months=month)
        string_date = start_date.strftime("%Y-%m")
        qss = [get_queryset(user, app, start_date) for app in settings.SUPERVISED_APPS]
        data.append([string_date] + [qs.count() for qs in qss])
        unique_patients.append([string_date] + [qs.values('patient').distinct().count() for qs in qss])

    return {'user_id': user.id,
            'data': data,
            'unique': unique_patients,
            }


def check_superuser(user):
    return user.is_superuser


@login_required(login_url='/login/')
@user_passes_test(check_superuser)
def index(request):
    context = get_users()
    #context = {'users_data': [get_summary_data(user['id']) for user in users['users']]}
    #context.update(users)
    return render(request, 'supervision/index.html', context)


@login_required(login_url='/login/')
@user_passes_test(check_superuser)
def user_data(request, user_id):
    return JsonResponse(get_summary_data(user_id))
