import os
from datetime import timedelta

# Get the path to the directory this file is in
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration"""
    # Secret key for sessions and CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-change-in-production'
    
    # SQLAlchemy database URI (use 'app.db' inside the main directory)
    # The database file will be stored in the root 'flaskrecords' directory
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Disable modification tracking (saves resources)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configure required extensions (if needed later)
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)