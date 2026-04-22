"""
WSGI config for dom_u_morya project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dom_u_morya.settings")

application = get_wsgi_application()

path = "/home/Begimai/dom_u_morya"
if path not in sys.path:
    sys.path.append(path)
