from django.db import models


class BlogPost(models.Model):
    PUBLISHED=1
    DRAFT=2
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
    )
    
    title = models.CharField(max_length=256)
    body = models.TextField()
    slug = models.SlugField()
    published_date = models.DateField(auto_now=True)
    published_status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)