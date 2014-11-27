# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Toilet.rating'
        db.delete_column(u'lavoratr_toilet', 'rating')

        # Deleting field 'Toilet.times_rated'
        db.delete_column(u'lavoratr_toilet', 'times_rated')

        # Adding field 'Toilet.positive_ratings'
        db.add_column(u'lavoratr_toilet', 'positive_ratings',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Toilet.negative_ratings'
        db.add_column(u'lavoratr_toilet', 'negative_ratings',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Toilet.rating'
        db.add_column(u'lavoratr_toilet', 'rating',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Toilet.times_rated'
        db.add_column(u'lavoratr_toilet', 'times_rated',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'Toilet.positive_ratings'
        db.delete_column(u'lavoratr_toilet', 'positive_ratings')

        # Deleting field 'Toilet.negative_ratings'
        db.delete_column(u'lavoratr_toilet', 'negative_ratings')


    models = {
        u'lavoratr.review': {
            'Meta': {'object_name': 'Review'},
            'comment_box': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'toilet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lavoratr.Toilet']"})
        },
        u'lavoratr.toilet': {
            'Meta': {'object_name': 'Toilet'},
            'accesible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'negative_ratings': ('django.db.models.fields.IntegerField', [], {}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'positive_ratings': ('django.db.models.fields.IntegerField', [], {}),
            'single_occupancy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'station': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'times_authenticated': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['lavoratr']
