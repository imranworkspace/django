"""
ASGI config for ModelForm_with_validations_error_messages project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelForm_with_validations_error_messages.settings')

application = get_asgi_application()
