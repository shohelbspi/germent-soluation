from django.apps import AppConfig


class FabricmanagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fabricmanagement"

    def ready(self):
        import fabricmanagement.signals
