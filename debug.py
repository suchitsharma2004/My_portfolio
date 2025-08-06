"""
Simple debugging script to identify the 500 error
This will help us understand what's failing on Vercel
"""

import os
import sys
import traceback

def debug_environment():
    """Debug the environment and Django setup"""
    debug_info = {
        'python_version': sys.version,
        'python_path': sys.path,
        'working_directory': os.getcwd(),
        'environment_variables': {
            'DEBUG': os.environ.get('DEBUG', 'NOT_SET'),
            'SECRET_KEY_SET': 'SECRET_KEY' in os.environ,
            'ALLOWED_HOSTS': os.environ.get('ALLOWED_HOSTS', 'NOT_SET'),
            'EMAIL_HOST_PASSWORD_SET': 'EMAIL_HOST_PASSWORD' in os.environ,
        },
        'django_status': 'NOT_TESTED'
    }
    
    # Test Django import
    try:
        # Add MacOS to path
        project_path = os.path.join(os.path.dirname(__file__), 'MacOS')
        if project_path not in sys.path:
            sys.path.insert(0, project_path)
        
        # Set Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MacOS.settings')
        
        # Test Django setup
        import django
        django.setup()
        debug_info['django_status'] = 'SUCCESS'
        debug_info['django_version'] = django.get_version()
        
        # Test WSGI import
        from MacOS.wsgi import application
        debug_info['wsgi_status'] = 'SUCCESS'
        
    except Exception as e:
        debug_info['django_status'] = 'FAILED'
        debug_info['django_error'] = str(e)
        debug_info['django_traceback'] = traceback.format_exc()
    
    return debug_info

# Simple WSGI application for debugging
def application(environ, start_response):
    """WSGI application with debugging"""
    try:
        # Add MacOS to path
        project_path = os.path.join(os.path.dirname(__file__), 'MacOS')
        if project_path not in sys.path:
            sys.path.insert(0, project_path)
        
        # Set Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MacOS.settings')
        
        # Try to import and use Django WSGI
        from MacOS.wsgi import application as django_app
        return django_app(environ, start_response)
        
    except Exception as e:
        # Return debugging information
        import json
        debug_info = debug_environment()
        debug_info['error'] = str(e)
        debug_info['error_type'] = type(e).__name__
        debug_info['traceback'] = traceback.format_exc()
        
        response_body = json.dumps(debug_info, indent=2).encode('utf-8')
        
        status = '500 Internal Server Error'
        headers = [
            ('Content-Type', 'application/json'),
            ('Access-Control-Allow-Origin', '*')
        ]
        
        start_response(status, headers)
        return [response_body]

# For Vercel
app = application

if __name__ == '__main__':
    # Local testing
    debug = debug_environment()
    import json
    print(json.dumps(debug, indent=2))
