# -*- coding: utf-8 -*-
from django.db.models import (
    Model, CharField, DateField, IntegerField,
)


class Customer(Model):
    """ Customer
    """
    first_name = CharField(verbose_name='First Name', max_length=100)
    last_name = CharField(verbose_name='Last Name', max_length=100)
    screen_name = CharField(verbose_name='Screen Name', max_length=30, unique=True)
    sex = IntegerField(verbose_name='Sex')
    birth_day = DateField(verbose_name='Birth Day')

    def __unicode__(self):
        return u'{}: {}, {}'.format(self.screen_name, self.first_name, self.last_name)

    class Meta:
        db_table = 'customer'
