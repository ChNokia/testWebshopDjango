from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('webshop.urls')),
    url(r'^index/', include('webshop.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^auth/', include('loginsys.urls')),
)# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
	#{'document_root': settings.MEDIA_ROOT}),
)