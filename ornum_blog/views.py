from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.contrib import messages

def blog_main_page(request, template='blog_base.html'):
    messages.success(request, 'this is a success')
    messages.warning(request, 'this is a warning')
    messages.error(request, 'this is a error')
    vars = RequestContext(request, {
        'foo': 'foobarbaz',
        'messages': messages,
    })
    return render_to_response(template, vars)