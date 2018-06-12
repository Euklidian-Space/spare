from .base import *  # noqa

import dj_database_url

DEBUG = False

# Recommended settings (Heroku takes care of this for us)
ALLOWED_HOSTS = ['*']

# Set database URL
db = dj_database_url.config(default=os.environ['DATABASE_URL'], conn_max_age=600)
db['ATOMIC_REQUESTS'] = True
DATABASES = {
    'default': db
}

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'public'

STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_DIRS = []

DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStorage'
