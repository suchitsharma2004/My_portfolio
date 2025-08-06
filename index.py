"""
Root-level entry point for Vercel deployment
This file imports the Django WSGI application
"""

import os
import sys

# Add the MacOS directory to the Python path
project_path = os.path.join(os.path.dirname(__file__), 'MacOS')
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MacOS.settings')

# Import Django first to ensure it's configured
import django
django.setup()

# Import the Django WSGI application
from MacOS.wsgi import application

# For Vercel compatibility - both 'app' and 'application' are available
app = application
