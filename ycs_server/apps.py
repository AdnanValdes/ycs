from django.apps import AppConfig
from django.conf import settings

class Ycs_serverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ycs_server'

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from ycs import operator
            operator.start()