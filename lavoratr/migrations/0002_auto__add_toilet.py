# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Toilet'
        db.create_table(u'lavoratr_toilet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('single_occupancy', self.gf('django.db.models.fields.BooleanField')()),
            ('accesible', self.gf('django.db.models.fields.BooleanField')()),
            ('station', self.gf('django.db.models.fields.BooleanField')()),
            ('comment_box', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'lavoratr', ['Toilet'])


    def backwards(self, orm):
        # Deleting model 'Toilet'
        db.delete_table(u'lavoratr_toilet')


    models = {
        u'lavoratr.toilet': {
            'Meta': {'object_name': 'Toilet'},
            'accesible': ('django.db.models.fields.BooleanField', [], {}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comment_box': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'single_occupancy': ('django.db.models.fields.BooleanField', [], {}),
            'station': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['lavoratr']