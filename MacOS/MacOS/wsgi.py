"""
WSGI config for MacOS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MacOS.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    print(f"WSGI Error: {e}")
    import traceback
    traceback.print_exc()
    raise

# Vercel compatibility
app = application
