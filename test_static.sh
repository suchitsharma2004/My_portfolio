#!/bin/bash

# Script to test static file collection locally before deployment

echo "Testing static file collection..."

# Activate virtual environment if it exists
if [ -d "myenv" ]; then
    source myenv/bin/activate
    echo "Virtual environment activated"
fi

# Navigate to Django project directory
cd MacOS

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

if [ $? -eq 0 ]; then
    echo "✅ Static files collected successfully!"
    echo "Files are in: staticfiles_build/static/"
    ls -la ../staticfiles_build/static/ 2>/dev/null || echo "Directory not found - check STATIC_ROOT setting"
else
    echo "❌ Error collecting static files"
    exit 1
fi

echo "Test completed!"
