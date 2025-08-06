"""
Root-level WSGI file for Vercel deployment
This file imports the actual WSGI application from the Django project
"""

import os
import sys

# Add the MacOS directory to the Python path
project_path = os.path.join(os.path.dirname(__file__), 'MacOS')
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Import the Django WSGI application
from MacOS.wsgi import application

# Vercel expects 'app' variable
app = application
