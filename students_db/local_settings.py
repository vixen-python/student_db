from .settings import *

DEBUG = True
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "students_db@local",
        "USER": "sda_student",
        "PASSWORD": "sda_student_password",
        "HOST": "127.0.0.1",
        "PORT": 3306
    }
}
"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# Media root

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')