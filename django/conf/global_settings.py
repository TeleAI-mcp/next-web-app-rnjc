#
# THIS FILE IS DEPRECATED!  It will be removed in Django 6.0.
#
# Use the following instead:
#     from django.conf import global_settings
#
# and refer to settings by their dotted path (e.g., global_settings.DEBUG).
#
# This module is provided for backwards compatibility only.
#

"""
Global settings for Django.

These settings control core Django behavior and are rarely changed.
"""

import os

# See https://docs.djangoproject.com/en/dev/ref/settings/

###################
# CORE SETTINGS     #
###################

# The root URLconf to use, for example "myproject.urls".
# By default, Django looks for a file named "urls.py" in the package
# specified by ROOT_URLCONF.
ROOT_URLCONF = ''

# A list of strings representing the host/domain names that this Django site
# can serve. This is a security measure to prevent HTTP Host header attacks.
# Values in this list can be fully qualified names (e.g. 'www.example.com'),
# in which case they will be matched against the request's Host header exactly
# (case-insensitive, not including port).
ALLOWED_HOSTS = []

# DEBUG is a boolean that turns on/off debug mode.
# Never deploy a site with DEBUG turned on.
DEBUG = False

# A string representing the email address error messages come from.
SERVER_EMAIL = 'root@localhost'

# A list of all the people who get code error notifications.
ADMINS = []

# A list in the same format as ADMINS that specifies who should get
# broken link (404) notifications when SEND_BROKEN_LINK_EMAILS=True.
MANAGERS = ADMINS

###################
# DATABASE SETTINGS #
###################

# Database connection settings.
# See https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.getcwd(), 'db.sqlite3'),
    }
}

# Default primary key field type.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####################
# CACHE SETTINGS    #
####################

# The cache backends to use.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = ''

####################
# AUTH SETTINGS     #
####################

# The model to use to store user accounts.
AUTH_USER_MODEL = 'auth.User'

# The class to use as the user backend.
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

# The number of days a password reset link is valid.
PASSWORD_RESET_TIMEOUT = 3 * 24 * 60 * 60

####################
# MIDDLEWARE SETTINGS#
####################

# List of middleware classes to use.
MIDDLEWARE = []

####################
# SECURITY SETTINGS #
####################

# Secret key for cryptographic signing.
SECRET_KEY = ''

# If True, the Secure cookie attribute is set on cookies.
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# If True, the HttpOnly cookie attribute is set on session cookies.
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False

# If True, the SameSite cookie attribute is set on cookies.
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

# Whether to use a secure cookie for the CSRF cookie.
CSRF_COOKIE_SECURE = False

# Whether to use HttpOnly for the CSRF cookie.
CSRF_COOKIE_HTTPONLY = False

####################
# EMAIL SETTINGS    #
####################

# Default email backend to use.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Default email address to use for various automated correspondence.
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# Subject-line prefix for email messages.
EMAIL_SUBJECT_PREFIX = '[Django] '

####################
# FILE UPLOADS      #
####################

# The maximum size, in bytes, that a file upload will be accepted before
# the DataLoss exception is raised.
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # 2.5 MB

# Directory where uploaded files are temporarily stored.
FILE_UPLOAD_TEMP_DIR = None

# The numeric mode to set newly-uploaded files to.
FILE_UPLOAD_PERMISSIONS = 0o644

# The numeric mode to set newly-uploaded directories to.
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

####################
# STATIC FILES      #
####################

# The absolute path to the directory static files should be collected to.
STATIC_ROOT = None

# The URL prefix for static files.
STATIC_URL = 'static/'

# List of locations of additional static files.
STATICFILES_DIRS = []

# The list of finder classes that know how to find static files.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

####################
# MEDIA FILES       #
####################

# The absolute path to the directory that holds media files.
MEDIA_ROOT = ''

# The URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = ''

####################
# LOCALE SETTINGS   #
####################

# A string representing the language code for this installation.
LANGUAGE_CODE = 'en-us'

# A list of languages to use for language selection.
LANGUAGES = [
    ('de', 'German'),
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('ko', 'Korean'),
    ('nl', 'Dutch'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ru', 'Russian'),
    ('tr', 'Turkish'),
    ('zh-hans', 'Simplified Chinese'),
    ('zh-hant', 'Traditional Chinese'),
]

# A list of locales to use for language selection.
LANGUAGES_BIDI = ['he', 'ar', 'fa', 'ur']

# The time zone to use when displaying dates.
TIME_ZONE = 'UTC'

# If True, Django will use timezone-aware datetimes.
USE_TZ = True

# If True, Django will format dates using the current locale.
USE_L10N = True

# If True, Django will use internationalized formats.
USE_I18N = True

####################
# MISC SETTINGS      #
####################

# The number of seconds before a page cache expires.
DEFAULT_PAGE_TEMPLATE = ''

# Whether to use the X-Forwarded-Host header.
USE_X_FORWARDED_HOST = False

# Whether to use the X-Forwarded-Port header.
USE_X_FORWARDED_PORT = False

# Whether to use ETags.
USE_ETAGS = False

# The number of seconds a request can be cached.
DEFAULT_CONTENT_TYPE = 'text/html'

# The default charset to use for all HttpResponse objects.
DEFAULT_CHARSET = 'utf-8'

# The name of the template to use for the 404 page.
DEFAULT_EXCEPTION_REPORTER_FILTER = 'django.views.debug.SafeExceptionReporterFilter'

# Whether to enable the debug toolbar.
INTERNAL_IPS = []

# Whether to enable the debug toolbar.
DEBUG_PROPAGATE_EXCEPTIONS = False

# Whether to enable the debug toolbar.
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Whether to enable the debug toolbar.
TEST_NON_SERIALIZED_APPS = []

# The number of seconds before a session expires.
SESSION_COOKIE_AGE = 1209600  # 2 weeks

# The name of the cookie to use for sessions.
SESSION_COOKIE_NAME = 'sessionid'

# The domain to use for session cookies.
SESSION_COOKIE_DOMAIN = None

# The path to use for session cookies.
SESSION_COOKIE_PATH = '/'

# Whether to save the session data on every request.
SESSION_SAVE_EVERY_REQUEST = False

# Whether to expire the session cookie when the user closes their browser.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# The serializer to use for session data.
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Whether to use a signed cookie for the session.
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# The file path to use for file-based sessions.
SESSION_FILE_PATH = None

# The cache backend to use for caching sessions.
SESSION_CACHE_ALIAS = 'default'

# The date format to use for date fields.
DATE_FORMAT = 'N j, Y'

# The time format to use for time fields.
TIME_FORMAT = 'P'

# The datetime format to use for datetime fields.
DATETIME_FORMAT = 'N j, Y, P'

# The short date format to use for date fields.
SHORT_DATE_FORMAT = 'm/d/Y'

# The short time format to use for time fields.
SHORT_DATETIME_FORMAT = 'm/d/Y P'

# The first day of the week.
FIRST_DAY_OF_WEEK = 0

# The decimal separator to use for decimal fields.
DECIMAL_SEPARATOR = '.'

# The thousands separator to use for decimal fields.
THOUSAND_SEPARATOR = ','

# The number of digits to group in numbers.
NUMBER_GROUPING = 3

# The XSS protection level to use.
X_FRAME_OPTIONS = 'SAMEORIGIN'

# The CSRF failure view to use.
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

# The CSRF trusted origins to use.
CSRF_TRUSTED_ORIGINS = []

# Whether to use a secure cookie for the CSRF cookie.
CSRF_COOKIE_SECURE = False

# Whether to use HttpOnly for the CSRF cookie.
CSRF_COOKIE_HTTPONLY = False

# The SameSite attribute to use for the CSRF cookie.
CSRF_COOKIE_SAMESITE = 'Lax'

# Whether to use a secure cookie for the session cookie.
SESSION_COOKIE_SECURE = False

# Whether to use HttpOnly for the session cookie.
SESSION_COOKIE_HTTPONLY = True

# The SameSite attribute to use for the session cookie.
SESSION_COOKIE_SAMESITE = 'Lax'

# Whether to use a secure cookie for the language cookie.
LANGUAGE_COOKIE_SECURE = False

# Whether to use HttpOnly for the language cookie.
LANGUAGE_COOKIE_HTTPONLY = False

# The SameSite attribute to use for the language cookie.
LANGUAGE_COOKIE_SAMESITE = 'Lax'

# The name of the cookie to use for the language cookie.
LANGUAGE_COOKIE_NAME = 'django_language'

# The age of the language cookie.
LANGUAGE_COOKIE_AGE = None

# The domain to use for the language cookie.
LANGUAGE_COOKIE_DOMAIN = None

# The path to use for the language cookie.
LANGUAGE_COOKIE_PATH = '/'

# Whether to use a signed cookie for the language cookie.
LANGUAGE_COOKIE_SECURE = False

# Whether to use HttpOnly for the language cookie.
LANGUAGE_COOKIE_HTTPONLY = False

# The SameSite attribute to use for the language cookie.
LANGUAGE_COOKIE_SAMESITE = 'Lax'

# The name of the cookie to use for the CSRF cookie.
CSRF_COOKIE_NAME = 'csrftoken'

# The age of the CSRF cookie.
CSRF_COOKIE_AGE = 31449600

# The domain to use for the CSRF cookie.
CSRF_COOKIE_DOMAIN = None

# The path to use for the CSRF cookie.
CSRF_COOKIE_PATH = '/'

# Whether to use a signed cookie for the CSRF cookie.
CSRF_COOKIE_SECURE = False

# Whether to use HttpOnly for the CSRF cookie.
CSRF_COOKIE_HTTPONLY = False

# The SameSite attribute to use for the CSRF cookie.
CSRF_COOKIE_SAMESITE = 'Lax'

# The name of the template to use for the 404 page.
IGNORABLE_404_URLS = [
    re.compile(r'^\.(php|cgi)$'),
    re.compile(r'^/phpmyadmin/'),
    re.compile(r'^/favicon\.ico$'),
]

# The name of the template to use for the 500 page.
SILENCED_SYSTEM_CHECKS = []

# The name of the template to use for the 403 page.
SECURE_BROWSER_XSS_FILTER = False

# The name of the template to use for the 404 page.
SECURE_CONTENT_TYPE_NOSNIFF = True

# The name of the template to use for the 404 page.
SECURE_HSTS_INCLUDE_SUBDOMAINS = False

# The name of the template to use for the 404 page.
SECURE_HSTS_PRELOAD = False

# The name of the template to use for the 404 page.
SECURE_HSTS_SECONDS = 0

# The name of the template to use for the 404 page.
SECURE_REDIRECT_EXEMPT = []

# The name of the template to use for the 404 page.
SECURE_SSL_HOST = None

# The name of the template to use for the 404 page.
SECURE_SSL_REDIRECT = False

# The name of the template to use for the 404 page.
SECURE_PROXY_SSL_HEADER = None

# The name of the template to use for the 404 page.
SIGNING_BACKEND = 'django.core.signing.TimestampSigner'

# The name of the template to use for the 404 page.
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# The name of the template to use for the 404 page.
DEFAULT_INDEX_TABLESPACE = ''

# The name of the template to use for the 404 page.
DEFAULT_TABLESPACE = ''

# The name of the template to use for the 404 page.
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440

# The name of the template to use for the 404 page.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

# The name of the template to use for the 404 page.
DATA_UPLOAD_MAX_NUMBER_FILES = 100

# The name of the template to use for the 404 page.
ABSOLUTE_URL_OVERRIDES = {}

# The name of the template to use for the 404 page.
EMAIL_HOST = 'localhost'

# The name of the template to use for the 404 page.
EMAIL_PORT = 25

# The name of the template to use for the 404 page.
EMAIL_HOST_USER = ''

# The name of the template to use for the 404 page.
EMAIL_HOST_PASSWORD = ''

# The name of the template to use for the 404 page.
EMAIL_USE_TLS = False

# The name of the template to use for the 404 page.
EMAIL_USE_SSL = False

# The name of the template to use for the 404 page.
EMAIL_SSL_CERTFILE = None

# The name of the template to use for the 404 page.
EMAIL_SSL_KEYFILE = None

# The name of the template to use for the 404 page.
EMAIL_TIMEOUT = None

# The name of the template to use for the 404 page.
EMAIL_LOCAL_HOST = None

# The name of the template to use for the 404 page.
FILE_CHARSET = 'utf-8'

# The name of the template to use for the 404 page.
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# The name of the template to use for the 404 page.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# The name of the template to use for the 404 page.
LOGGING = {}

# The name of the template to use for the 404 page.
LOGGING_CONFIG = 'logging.config.dictConfig'

# The name of the template to use for the 404 page.
MANAGED_FILES = False

# The name of the template to use for the 404 page.
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# The name of the template to use for the 404 page.
MONTH_DAY_FORMAT = 'F j'

# The name of the template to use for the 404 page.
NUMBER_GROUPING = 0

# The name of the template to use for the 404 page.
PREPEND_WWW = False

# The name of the template to use for the 404 page.
ROOT_URLCONF = ''

# The name of the template to use for the 404 page.
SECRET_KEY = ''

# The name of the template to use for the 404 page.
SECURE_BROWSER_XSS_FILTER = False

# The name of the template to use for the 404 page.
SECURE_CONTENT_TYPE_NOSNIFF = True

# The name of the template to use for the 404 page.
SECURE_HSTS_INCLUDE_SUBDOMAINS = False

# The name of the template to use for the 404 page.
SECURE_HSTS_PRELOAD = False

# The name of the template to use for the 404 page.
SECURE_HSTS_SECONDS = 0

# The name of the template to use for the 404 page.
SECURE_REDIRECT_EXEMPT = []

# The name of the template to use for the 404 page.
SECURE_SSL_HOST = None

# The name of the template to use for the 404 page.
SECURE_SSL_REDIRECT = False

# The name of the template to use for the 404 page.
SECURE_PROXY_SSL_HEADER = None

# The name of the template to use for the 404 page.
SEND_BROKEN_LINK_EMAILS = False

# The name of the template to use for the 404 page.
SERIALIZATION_MODULES = {
    'json': 'django.core.serializers.json',
    'xml': 'django.core.serializers.xml_serializer',
}

# The name of the template to use for the 404 page.
SERVER_EMAIL = 'root@localhost'

# The name of the template to use for the 404 page.
SHORT_DATE_FORMAT = 'm/d/Y'

# The name of the template to use for the 404 page.
SHORT_DATETIME_FORMAT = 'm/d/Y P'

# The name of the template to use for the 404 page.
SIGNING_BACKEND = 'django.core.signing.TimestampSigner'

# The name of the template to use for the 404 page.
SILENCED_SYSTEM_CHECKS = []

# The name of the template to use for the 404 page.
STATICFILES_DIRS = []

# The name of the template to use for the 404 page.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# The name of the template to use for the 404 page.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# The name of the template to use for the 404 page.
STORAGES = {}

# The name of the template to use for the 404 page.
TEMPLATES = []

# The name of the template to use for the 404 page.
TEST_NON_SERIALIZED_APPS = []

# The name of the template to use for the 404 page.
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# The name of the template to use for the 404 page.
TIME_FORMAT = 'P'

# The name of the template to use for the 404 page.
TIME_INPUT_FORMATS = [
    '%H:%M:%S',    # '14:30:59'
    '%H:%M:%S.%f', # '14:30:59.000200'
    '%H:%M',       # '14:30'
]

# The name of the template to use for the 404 page.
TIME_ZONE = 'UTC'

# The name of the template to use for the 404 page.
USE_I18N = True

# The name of the template to use for the 404 page.
USE_L10N = True

# The name of the template to use for the 404 page.
USE_THOUSAND_SEPARATOR = False

# The name of the template to use for the 404 page.
USE_TZ = True

# The name of the template to use for the 404 page.
USE_X_FORWARDED_HOST = False

# The name of the template to use for the 404 page.
USE_X_FORWARDED_PORT = False

# The name of the template to use for the 404 page.
WSGI_APPLICATION = None

# The name of the template to use for the 404 page.
YEAR_MONTH_FORMAT = 'F Y'
