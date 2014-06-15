# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table(u'picrev_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('passkey', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('signed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('submitted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=150, db_index=True)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('answered', self.gf('django.db.models.fields.DateTimeField')(default=None, blank=True)),
        ))
        db.send_create_signal(u'picrev', ['Request'])

        # Adding model 'Image'
        db.create_table(u'picrev_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picrev.Request'])),
            ('source', self.gf('django.db.models.fields.CharField')(default='REQ', max_length=3)),
        ))
        db.send_create_signal(u'picrev', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table(u'picrev_request')

        # Deleting model 'Image'
        db.delete_table(u'picrev_image')


    models = {
        u'picrev.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picrev.Request']"}),
            'source': ('django.db.models.fields.CharField', [], {'default': "'REQ'", 'max_length': '3'})
        },
        u'picrev.request': {
            'Meta': {'object_name': 'Request'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answered': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'passkey': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'signed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_index': 'True'}),
            'submitted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['picrev']