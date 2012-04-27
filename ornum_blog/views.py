from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.contrib import messages

from ornum_blog.models import BlogPost

def post_list_page(request, template='post_list.html'):
    
    posts = BlogPost.objects.all().order_by('published_date')
    
    vars = RequestContext(request, {
        'posts': posts,
    })
    return render_to_response(template, vars)
    
def post_page(request, 
    post_slug=None,
    template='post.html'):

    post = get_object_or_404(BlogPost, slug=post_slug)
    
    vars = RequestContext(request, {
        'post': post,
        })
    return render_to_response(template, vars)