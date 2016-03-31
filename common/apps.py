import os
from common.localization import verbose_name_app
from django.apps import AppConfig

def app_name(filename):
    print(filename)
    return os.path.basename(os.path.normpath(os.path.dirname(os.path.realpath(filename))))

def common_app_config(filename):
    def wrap(f):
        class CommonAppConfig(AppConfig):
            name = app_name(filename)
            verbose_name = verbose_name_app(name)
        return CommonAppConfig
    return wrap
