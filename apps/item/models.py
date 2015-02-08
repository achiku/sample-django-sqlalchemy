# -*- coding: utf-8 -*-
from django.db.models import (
    Model, CharField, IntegerField, ManyToManyField,
    DateTimeField, ForeignKey,
)


class Item(Model):
    """ Item
    """
    name = CharField(verbose_name='Item Name', max_length=100)
    price = IntegerField(verbose_name='Price')

    class Meta:
        db_table = 'item'


class ItemCategory(Model):
    """ Item category
    """
    name = CharField(verbose_name='Category Name', max_length=100)
    items = ManyToManyField(Item, through='ItemCategoryRelation')

    class Meta:
        db_table = 'item_category'


class ItemCategoryRelation(Model):
    """ Relationship between item and its category
    """
    created = DateTimeField()
    item = ForeignKey(Item)
    category = ForeignKey(ItemCategory)

    class Meta:
        db_table = 'item_category_relation'
