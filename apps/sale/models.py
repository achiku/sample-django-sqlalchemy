# -*- coding: utf-8 -*-
from django.db.models import (
    Model, DateTimeField, ForeignKey, IntegerField,
)
from apps.customer.models import Customer
from apps.item.models import Item


class Sale(Model):
    """ Sales
    """
    time = DateTimeField(verbose_name='Time Sold')
    price = IntegerField(verbose_name='Price')
    customer = ForeignKey(Customer, verbose_name='Customer', related_name='sales')

    def __unicode__(self):
        return u'{}, {}'.format(self.time, self.customer.screen_name)

    class Meta:
        db_table = 'sale'


class SaleDetail(Model):
    """ Sales detail
    """
    sale = ForeignKey(Sale, related_name='details')
    item = ForeignKey(Item, verbose_name='Item', related_name='sales_details')
    price = IntegerField(verbose_name='Price')
    count = IntegerField(verbose_name='#Items')

    def __unicode__(self):
        return u'{}, {}, {}'.format(self.item.name, self.count, self.price)

    class Meta:
        db_table = 'sale_detail'
