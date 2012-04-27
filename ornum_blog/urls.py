from django.conf.urls import patterns, include, url
from ornum_blog.views import *

urlpatterns = patterns('',
    url(r'^$', 
        post_list_page,
        name="post_list_page"),
    url(r'(?P<post_slug>[-\w]+)/$',
        post_page,
        name="post_page"),
        
)
