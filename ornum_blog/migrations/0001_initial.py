# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BlogPost'
        db.create_table('ornum_blog_blogpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('published_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('published_status', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal('ornum_blog', ['BlogPost'])


    def backwards(self, orm):
        
        # Deleting model 'BlogPost'
        db.delete_table('ornum_blog_blogpost')


    models = {
        'ornum_blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published_status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['ornum_blog']
