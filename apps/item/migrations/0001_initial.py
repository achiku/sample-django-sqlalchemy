# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table('item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'item', ['Item'])

        # Adding model 'ItemCategory'
        db.create_table('item_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'item', ['ItemCategory'])

        # Adding model 'ItemCategoryRelation'
        db.create_table('item_category_relation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.Item'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.ItemCategory'])),
        ))
        db.send_create_signal(u'item', ['ItemCategoryRelation'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table('item')

        # Deleting model 'ItemCategory'
        db.delete_table('item_category')

        # Deleting model 'ItemCategoryRelation'
        db.delete_table('item_category_relation')


    models = {
        u'item.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'item'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'item.itemcategory': {
            'Meta': {'object_name': 'ItemCategory', 'db_table': "'item_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['item.Item']", 'through': u"orm['item.ItemCategoryRelation']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'item.itemcategoryrelation': {
            'Meta': {'object_name': 'ItemCategoryRelation', 'db_table': "'item_category_relation'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.ItemCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.Item']"})
        }
    }

    complete_apps = ['item']