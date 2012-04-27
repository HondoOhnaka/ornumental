from django.contrib import admin 
from ornum_blog.models import * 

class BlogPostAdmin(admin.ModelAdmin): 
    pass 

admin.site.register(BlogPost, BlogPostAdmin)
