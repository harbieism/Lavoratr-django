# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'lavoratr_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('toilet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lavoratr.Toilet'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('comment_box', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
        ))
        db.send_create_signal(u'lavoratr', ['Review'])

        # Deleting field 'Toilet.comment_box'
        db.delete_column(u'lavoratr_toilet', 'comment_box')

        # Adding field 'Toilet.times_authenticated'
        db.add_column(u'lavoratr_toilet', 'times_authenticated',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'lavoratr_review')

        # Adding field 'Toilet.comment_box'
        db.add_column(u'lavoratr_toilet', 'comment_box',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=127, blank=True),
                      keep_default=False)

        # Deleting field 'Toilet.times_authenticated'
        db.delete_column(u'lavoratr_toilet', 'times_authenticated')


    models = {
        u'lavoratr.review': {
            'Meta': {'object_name': 'Review'},
            'comment_box': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'toilet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lavoratr.Toilet']"})
        },
        u'lavoratr.toilet': {
            'Meta': {'object_name': 'Toilet'},
            'accesible': ('django.db.models.fields.BooleanField', [], {}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'times_authenticated': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'times_rated': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['lavoratr']
