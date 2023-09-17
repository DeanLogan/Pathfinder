from django.apps import AppConfig

class DatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'database'

    def ready(self):
        import database.signals  # Replace with the actual path to your signals.py file
