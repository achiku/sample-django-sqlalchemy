# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sale'
        db.create_table(u'sale_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_sold', self.gf('django.db.models.fields.DateTimeField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sales', to=orm['item.Item'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sales', to=orm['customer.Customer'])),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'sale', ['Sale'])


    def backwards(self, orm):
        # Deleting model 'Sale'
        db.delete_table(u'sale_sale')


    models = {
        u'customer.customer': {
            'Meta': {'object_name': 'Customer', 'db_table': "'customer'"},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'item.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'item'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sale.sale': {
            'Meta': {'object_name': 'Sale'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sales'", 'to': u"orm['customer.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sales'", 'to': u"orm['item.Item']"}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'time_sold': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['sale']