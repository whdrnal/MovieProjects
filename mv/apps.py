from django.apps import AppConfig


class MvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mv'

    def ready(self):
        import mv.signals
