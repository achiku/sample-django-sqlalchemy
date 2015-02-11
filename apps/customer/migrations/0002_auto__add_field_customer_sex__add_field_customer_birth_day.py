# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Customer.sex'
        db.add_column('customer', 'sex',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Customer.birth_day'
        db.add_column('customer', 'birth_day',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 2, 11, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Customer.sex'
        db.delete_column('customer', 'sex')

        # Deleting field 'Customer.birth_day'
        db.delete_column('customer', 'birth_day')


    models = {
        u'customer.customer': {
            'Meta': {'object_name': 'Customer', 'db_table': "'customer'"},
            'birth_day': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'sex': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['customer']