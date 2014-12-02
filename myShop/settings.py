# -*- coding: utf-8 -*-

"""
Django settings for myShop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'myShop/templates'), )

WEB_SITE_NAME = 'My WebSHop'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')6g@c==+)%(xk9p6zxe*bpio4n$z@3m#fll^hjhl=@h0)+fb(2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cart',
    'webshop',
    'utils',
    'loginsys',
    'tinymce',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.CacheMiddleware',
)

#CACHES = {
#    'default': {
 #       'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
  #  }
#}

ROOT_URLCONF = 'myShop.urls'

WSGI_APPLICATION = 'myShop.wsgi.application'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 1
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'webshop/static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'webshop/media/')#BASE_DIR + '/webshop/media/'
MEDIA_URL = '/media/'

#AUTHENTICATION_BACKENDS = (
 #   'webshop.auth_backends.CustomUserModelBackend',
 #   'django.contrib.auth.backends.ModelBackend',
#)

#CUSTOM_USER_MODEL = 'webshop.models.Customer'

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.


TINYMCE_JS_URL = MEDIA_URL + "tinymce/media/tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = MEDIA_ROOT + "/tinymce/media/tiny_mce"

TINYMCE_SPELLCHECKER=False

TINYMCE_PLUGINS = [
    'safari',
    'table',
    'advlink',
    'advimage',
    'iespell',
    'inlinepopups',
    'media',
    'searchreplace',
    'contextmenu',
    'paste',
    'wordcount'
]

TINYMCE_DEFAULT_CONFIG={
    'theme' : "advanced",
    'plugins' : ",".join(TINYMCE_PLUGINS), # django-cms
    'language' : 'ukr',
    "theme_advanced_buttons1" : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect,|,spellchecker",
    "theme_advanced_buttons2" : "cut,copy,paste,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,image,cleanup,code,|,forecolor,backcolor,|,insertfile,insertimage",
    "theme_advanced_buttons3" : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : True,
    'table_default_cellpadding': 2,
    'table_default_cellspacing': 2,
    'cleanup_on_startup' : False,
    'cleanup' : False,
    'paste_auto_cleanup_on_paste' : False,
    'paste_block_drop' : False,
    'paste_remove_spans' : False,
    'paste_strip_class_attributes' : False,
    'paste_retain_style_properties' : "",
    'forced_root_block' : False,
    'force_br_newlines' : False,
    'force_p_newlines' : False,
    'remove_linebreaks' : False,
    'convert_newlines_to_brs' : False,
    'inline_styles' : False,
    'relative_urls' : False,
    'formats' : {
        'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
        'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
        'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
        'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
        'strikethrough' : {'inline' : 'del'},
        'italic' : {'inline' : 'em'},
        'bold' : {'inline' : 'strong'},
        'underline' : {'inline' : 'u'}
    },
    'pagebreak_separator' : "",
    # Drop lists for link/image/media/template dialogs
    'template_external_list_url': 'lists/template_list.js',
    'external_link_list_url': 'lists/link_list.js',
    'external_image_list_url': 'lists/image_list.js',
    'media_external_list_url': 'lists/media_list.js',
    #
    #'file_browser_callback':'tinyDjangoBrowser'
}

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'utils.context_processors.webshop',
)

SUIT_CONFIG = {
    'MENU': (

        # Keep original label and models
        'sites',

        # Rename app and set icon
        {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},

        # Reorder app models
        {'app': 'auth', 'models': ('user', 'group')},

        # Custom app, with models
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},

        # Cross-linked models with custom name; Hide default icon
        {'label': 'Custom', 'icon':None, 'models': (
            'auth.group',
            {'model': 'auth.user', 'label': 'Staff'}
        )},

        # Custom app, no models (child links)
        {'label': 'Users', 'url': 'auth.user', 'icon':'icon-user'},

        # Separator
        '-',

        # Custom app and model with permissions
        {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
            {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
        ]},
    )
}

TEMPLATE_DIRS = (
    BASE_DIR + '/myShop/templates',
    #BASE_DIR + '/loginsys/templates',
)

AUTH_PROFILE_MODULE = 'webshop.Customer'
#STATICFILES_DIRS = (
 #   '/home/ubuntu/Desktop/Form_files/myShop/',
#)
