# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Toilet.times_rated'
        db.add_column(u'lavoratr_toilet', 'times_rated',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Toilet.times_rated'
        db.delete_column(u'lavoratr_toilet', 'times_rated')


    models = {
        u'lavoratr.toilet': {
            'Meta': {'object_name': 'Toilet'},
            'accesible': ('django.db.models.fields.BooleanField', [], {}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comment_box': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'single_occupancy': ('django.db.models.fields.BooleanField', [], {}),
            'station': ('django.db.models.fields.BooleanField', [], {}),
            'times_rated': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['lavoratr']