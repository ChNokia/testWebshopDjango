# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.date_add'
        db.add_column('webshop_category', 'date_add',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 20, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.date_add'
        db.add_column('webshop_product', 'date_add',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 20, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.date_add'
        db.delete_column('webshop_category', 'date_add')

        # Deleting field 'Product.date_add'
        db.delete_column('webshop_product', 'date_add')


    models = {
        'webshop.category': {
            'Meta': {'object_name': 'Category'},
            'date_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 20, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'meta_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'orderin': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['webshop.Category']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'webshop.customer': {
            'Meta': {'object_name': 'Customer'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 20, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_visited': ('django.db.models.fields.DateTimeField', [], {}),
            'discaunt': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'webshop.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product'", 'to': "orm['webshop.Category']"}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 20, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'meta_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'meta_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'orderin': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'price_in_ua': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'webshop.productimages': {
            'Meta': {'object_name': 'ProductImages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['webshop.Product']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['webshop']