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

try:
    # Import the Django WSGI application
    from MacOS.wsgi import application
    
    # For Vercel compatibility - both 'app' and 'application' are checked
    app = application
    
except Exception as e:
    # Error handling for debugging
    def application(environ, start_response):
        import json
        response_body = json.dumps({
            'error': f'Django import failed: {str(e)}',
            'error_type': type(e).__name__,
            'python_path': sys.path,
            'working_directory': os.getcwd()
        }).encode('utf-8')
        
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'application/json')]
        
        start_response(status, headers)
        return [response_body]
    
    app = application
