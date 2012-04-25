import os

from django.views.generic import TemplateView

from django.conf.urls import patterns, include, url
from django.contrib import admin
from ornumental import settings

from ornumental.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('ornum_blog.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    
    static_dir = os.path.join(
        os.path.dirname(__file__), 'static'
    )
    
    media_dir = os.path.join(
        os.path.dirname(__file__), 'media'
    )   
    
    urlpatterns += patterns('',
    
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': static_dir }),
    
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': media_dir }),
    )
    
