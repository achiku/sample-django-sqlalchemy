# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StockHistory.stock'
        db.add_column('stock_history', 'stock',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['stock.Stock']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StockHistory.stock'
        db.delete_column('stock_history', 'stock_id')


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
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stock.Stock']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['stock']