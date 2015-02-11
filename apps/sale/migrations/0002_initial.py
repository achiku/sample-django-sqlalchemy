# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sale'
        db.create_table('sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sales', to=orm['customer.Customer'])),
        ))
        db.send_create_signal(u'sale', ['Sale'])

        # Adding model 'SaleDetail'
        db.create_table('sale_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sale', self.gf('django.db.models.fields.related.ForeignKey')(related_name='details', to=orm['sale.Sale'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sales_details', to=orm['item.Item'])),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'sale', ['SaleDetail'])


    def backwards(self, orm):
        # Deleting model 'Sale'
        db.delete_table('sale')

        # Deleting model 'SaleDetail'
        db.delete_table('sale_detail')


    models = {
        u'customer.customer': {
            'Meta': {'object_name': 'Customer', 'db_table': "'customer'"},
            'birth_day': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'sex': ('django.db.models.fields.IntegerField', [], {})
        },
        u'item.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'item'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sale.sale': {
            'Meta': {'object_name': 'Sale', 'db_table': "'sale'"},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sales'", 'to': u"orm['customer.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'sale.saledetail': {
            'Meta': {'object_name': 'SaleDetail', 'db_table': "'sale_detail'"},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sales_details'", 'to': u"orm['item.Item']"}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'sale': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'details'", 'to': u"orm['sale.Sale']"})
        }
    }

    complete_apps = ['sale']