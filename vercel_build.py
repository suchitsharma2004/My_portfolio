#!/usr/bin/env python
"""
Vercel build script for Django
This script handles the build process for Vercel deployment
"""

import os
import sys
import subprocess

def main():
    print("Starting Vercel build process...")
    
    # Change to the Django project directory
    os.chdir('MacOS')
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MacOS.settings')
    
    # Import Django
    try:
        import django
        django.setup()
        print("Django setup completed")
    except ImportError as exc:
        print(f"Django import error: {exc}")
        sys.exit(1)
    
    # Collect static files
    try:
        from django.core.management import execute_from_command_line
        print("Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])
        print("Static files collected successfully")
    except Exception as exc:
        print(f"Error collecting static files: {exc}")
        sys.exit(1)
    
    print("Build process completed successfully!")

if __name__ == '__main__':
    main()
