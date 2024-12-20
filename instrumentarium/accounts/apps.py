from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instrumentarium.accounts'

    def ready(self):
        import instrumentarium.accounts.signals
