# -*- coding: utf-8 -*-
from datetime import datetime
import factory
from factory.django import DjangoModelFactory
from apps.item.models import (
   Item, ItemCategory, ItemCategoryRelation,
)


class ItemFactory(DjangoModelFactory):
    """ ItemFactory
    """
    class Meta:
        model = Item

    name = factory.Sequence(lambda n: 'item #{}'.format(n))
    price = factory.Iterator([200, 100, 300, 100])


class ItemCategoryFactory(DjangoModelFactory):
    """ ItemCategoryFactory
    """
    class Meta:
        model = ItemCategory

    name = factory.Sequence(lambda n: 'item category #{}'.format(n))


class ItemCategoryRelationFactory(DjangoModelFactory):
    """ ItemCategoryRelationFactory
    """
    class Meta:
        model = ItemCategoryRelation

    created = datetime.now()
    item = factory.SubFactory(ItemFactory)
    category = factory.SubFactory(ItemCategoryFactory)


class ItemWithCategoryFactory(ItemFactory):
    """ for m2m relation of item and category
    """
    items = factory.RelatedFactory(ItemCategoryRelationFactory, 'item')


class CategoryWithItemFactory(ItemCategoryFactory):
    """ for m2m relation of item and category
    """
    categories = factory.RelatedFactory(ItemCategoryRelationFactory, 'category')
