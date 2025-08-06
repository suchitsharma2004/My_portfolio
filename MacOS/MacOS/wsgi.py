"""
WSGI config for MacOS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MacOS.settings')

# Collect static files for Vercel deployment
try:
    import django
    django.setup()
    
    from django.core.management import execute_from_command_line
    from django.conf import settings
    
    # Only collect static files if not in DEBUG mode (production)
    if not settings.DEBUG:
        try:
            execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])
        except Exception as e:
            print(f"Warning: Could not collect static files: {e}")
except Exception as e:
    print(f"Warning: Static file collection failed: {e}")

application = get_wsgi_application()

# Vercel compatibility
app = application
