from django.conf.urls import patterns, include, url
from ornum_blog.views import *

urlpatterns = patterns('',
    url(r'^$', blog_main_page,
    name="blog_main_page"),
)
