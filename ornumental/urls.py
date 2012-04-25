from django.conf.urls import patterns, include, url
from django.contrib import admin

from ornumental.views import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', home_page,
        name="home_page"),
    url(r'^about/$', about_page,
        name="about_page"),
        
    url(r'^blog/$', include('ornum_blog.urls')),
    
    (r'^contact/', include('contact_form.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
