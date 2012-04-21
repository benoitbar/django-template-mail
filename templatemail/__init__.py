from django.conf import settings


settings.EMAIL_HTML2TEXT = getattr(settings, 'EMAIL_HTML2TEXT', None)
