# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stock'
        db.create_table('stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.Item'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'stock', ['Stock'])

        # Adding model 'StockHistory'
        db.create_table('stock_history', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.Item'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'stock', ['StockHistory'])


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table('stock')

        # Deleting model 'StockHistory'
        db.delete_table('stock_history')


    models = {
        u'item.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'item'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'stock.stock': {
            'Meta': {'object_name': 'Stock', 'db_table': "'stock'"},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.Item']"})
        },
        u'stock.stockhistory': {
            'Meta': {'object_name': 'StockHistory', 'db_table': "'stock_history'"},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.Item']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['stock']