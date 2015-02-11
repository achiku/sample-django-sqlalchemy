# -*- coding: utf-8 -*-
from django.db.models import (
    Model, ForeignKey, IntegerField, DateTimeField,
)
from apps.item.models import Item


class Stock(Model):
    """ Stock
    """
    item = ForeignKey(Item, verbose_name='Item')
    count = IntegerField(null=False)

    class Meta:
        db_table = 'stock'


class StockHistory(Model):
    """ Stock history
    """
    time = DateTimeField(null=False)
    stock = ForeignKey(
        Stock, verbose_name='Stock',
        null=False, related_name='details')
    item = ForeignKey(
        Item, verbose_name='Item',
        null=False, related_name='stock_histries')
    count = IntegerField(null=False)

    def __unicode__(self):
        return u'{} {} {}'.format(self.time, self.item, self.count)

    class Meta:
        db_table = 'stock_history'
