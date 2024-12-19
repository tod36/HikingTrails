import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)

class HikersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HikingTrails.Hikers'

    def ready(self):
        import HikingTrails.Hikers.signals
        logger.info("HikersConfig ready method called, signals imported.")