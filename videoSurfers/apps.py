from django.apps import AppConfig


class VideosurfersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videoSurfers'

    def ready(self) -> None:
      from . import signals  # register signals