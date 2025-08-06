#!/bin/bash

# Build script for Vercel deployment
echo "Starting build process..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python MacOS/manage.py collectstatic --noinput --clear

echo "Build completed successfully!"
