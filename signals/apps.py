from django.apps import AppConfig

from signals.i18n.hooks import process_translate_decorators


class SignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "signals"

    def ready(self):
        process_translate_decorators()
