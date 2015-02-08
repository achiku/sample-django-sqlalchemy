# -*- coding: utf-8 -*-
from django.db.models import (
    Model, CharField,
)


class Customer(Model):
    """ Customer
    """
    first_name = CharField(verbose_name='First Name', max_length=100)
    last_name = CharField(verbose_name='Last Name', max_length=100)
    screen_name = CharField(verbose_name='Screen Name', max_length=30, unique=True)

    class Meta:
        db_table = 'customer'
