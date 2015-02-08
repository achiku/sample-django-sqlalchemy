# -*- coding: utf-8 -*-
from django.db.models import (
    Model, DateTimeField, ForeignKey, IntegerField
)
from apps.customer.models import Customer
from apps.item.models import Item


class Sale(Model):
    """ Sale Event
    """
    time_sold = DateTimeField(verbose_name='Time Sold')
    item = ForeignKey(Item, verbose_name='Item', related_name='sales')
    customer = ForeignKey(Customer, verbose_name='customer', related_name='sales')
    price = IntegerField(verbose_name='Price')
