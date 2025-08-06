# macOS Portfolio - Vercel Deployment Guide

## � Deployment Checklist

### 1. Files Added for Vercel Deployment
- ✅ `vercel.json` - Simplified Vercel configuration (no builds section)
- ✅ `app.py` - Root-level WSGI wrapper for Vercel
- ✅ `build_files.sh` - Simple build script  
- ✅ `requirements.txt` - Python dependencies (includes whitenoise)
- ✅ `.env.vercel.template` - Environment variables template (safe to commit)
- ✅ `.env.production` - Your actual env file (in .gitignore - NOT committed)
- ✅ Updated `settings.py` - Production settings with WhiteNoise + debugging
- ✅ Updated `wsgi.py` - Enhanced error handling
- ✅ Added `/health/` endpoint for debugging

### 2. Environment Variables to Set in Vercel

Go to your Vercel project dashboard → Settings → Environment Variables and add:

**Required Variables:**
```
DEBUG=False
SECRET_KEY=your-new-production-secret-key-here
ALLOWED_HOSTS=your-vercel-domain.vercel.app,localhost,127.0.0.1
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

**How to get these values:**

1. **SECRET_KEY**: Generate a new one using:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **ALLOWED_HOSTS**: Replace `your-vercel-domain` with your actual Vercel domain
   - Example: `my-portfolio-123.vercel.app,localhost,127.0.0.1`

3. **EMAIL_HOST_PASSWORD**: Your Gmail App Password (16 characters, no spaces)

### Local Development:
1. Copy `.env.example` to `.env`
2. Fill in your actual credentials
3. Never commit `.env` to git

### Security Notes:
- ✅ `.env` is in `.gitignore`
- ✅ Use `.env.example` for documentation
- ✅ Set environment variables in Vercel dashboard
- ✅ Use different SECRET_KEY for production

### Gmail Setup:
1. Enable 2-Step Verification
2. Generate App Password for Mail
3. Use 16-character app password (not your Gmail password)

## 📧 Email Configuration:
- Development: Uses local .env file
- Production: Uses Vercel environment variables
- Emails sent to: suchit.sharma.delhi@gmail.com

## 🔧 **Troubleshooting Fixed**

**Previous Error:** `WSGI application 'MacOS.wsgi.application' could not be loaded`

**Root Cause:** Missing WhiteNoise dependency in requirements.txt causing WSGI import failure.

**Fix Applied:**
1. ✅ Added specific WhiteNoise version (6.6.0) to requirements.txt
2. ✅ Updated Django STORAGES configuration for Django 5.2+
3. ✅ Simplified WSGI file to avoid startup complexity
4. ✅ Tested WSGI loading and static file collection locally

---

**New Error:** `500: INTERNAL_SERVER_ERROR - FUNCTION_INVOCATION_FAILED`

**Potential Causes & Fixes Applied:**
1. ✅ Added fallback environment variable handling (doesn't rely on python-decouple)
2. ✅ Added debugging to WSGI and settings files
3. ✅ Added error handling for email configuration
4. ✅ Added fallback for STORAGES configuration
5. ✅ Added all required dependencies to requirements.txt

**Debug Steps Added:**
- Environment variable debugging in settings.py
- Error handling in WSGI file with traceback
- Graceful fallbacks for all external dependencies

**Current Status:** ✅ **Ready for Vercel Deployment with Enhanced Debugging**

---

**Latest Warning:** `Due to builds existing in your configuration file, the Build and Development Settings defined in your Project Settings will not apply`

**Fix Applied:**
1. ✅ Removed `builds` section from vercel.json
2. ✅ Created root-level `app.py` WSGI wrapper
3. ✅ Simplified vercel.json to use `functions` instead of `builds`
4. ✅ Let Vercel handle automatic build detection

**Current vercel.json:**
```json
{
  "version": 2,
  "functions": {
    "app.py": {
      "runtime": "python3.9"
    }
  }
}
```

**Current Status:** ✅ **Ready for Vercel Deployment with Simplified Configuration**

**Debug Steps:**
1. Deploy these changes
2. Check `/health/` endpoint for debug info
3. Check Vercel function logs for any remaining errors
