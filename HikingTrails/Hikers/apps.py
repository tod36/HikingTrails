from django.apps import AppConfig


class HikersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HikingTrails.Hikers'

    # def ready(self):
    #     import HikingTrails.Hikers.signals
