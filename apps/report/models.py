# -*- coding: utf-8 -*-
from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=100)

    class Meta:
        db_table = 'item'


class ItemCategory(modesl.Model):
    name = models.CharField(verbose_name='カテゴリ名', max_length=100)
    items = modesl.ManyToMany(Item, through='ItemCategoryRelation')

    class Meta:
        db_table = 'item_category'


class ItemCategoryRelation(models.Model):
    created = models.DateTimeField()
    item = models.ForeignKey(Item)
    category = models.ForeignKey(ItemCategory)

    class Meta:
        db_table = 'item_category_relation'
