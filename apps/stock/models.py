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
    item = ForeignKey(Item, verbose_name='Item', null=False)
    count = IntegerField(null=False)

    class Meta:
        db_table = 'stock_history'
