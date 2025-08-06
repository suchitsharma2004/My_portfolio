# macOS Portfolio - Vercel Deployment Guide

## � Deployment Checklist

### 1. Files Added for Vercel Deployment
- ✅ `vercel.json` - Vercel configuration
- ✅ `build_files.sh` - Build script for static files
- ✅ `requirements.txt` - Python dependencies
- ✅ `.env.vercel.template` - Environment variables template (safe to commit)
- ✅ `.env.production` - Your actual env file (in .gitignore - NOT committed)
- ✅ Updated `settings.py` - Production settings
- ✅ Updated `wsgi.py` - Vercel compatibility

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
