from common.apps import default_app_config_string, common_app_config
default_app_config = default_app_config_string(__file__)


@common_app_config(__file__)
class AppConfig(object):
    pass
