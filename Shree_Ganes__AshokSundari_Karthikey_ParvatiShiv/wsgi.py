"""
WSGI config for Shree_Ganes__AshokSundari_Karthikey_ParvatiShiv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shree_Ganes__AshokSundari_Karthikey_ParvatiShiv.settings')

application = get_wsgi_application()
