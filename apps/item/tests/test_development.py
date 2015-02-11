# -*- coding: utf-8 -*-
import pytest
from apps.item.models import Item, ItemCategory
from tests.factories.item import (
    ItemWithCategoryFactory, CategoryWithItemFactory,
)

pytestmark = pytest.mark.django_db


def test_item():
    """ Factory and Model development driver
    """
    ItemWithCategoryFactory.create_batch(2)
    for i in Item.objects.all():
        print '{}: {}'.format(i.name, i.price)
        for c in i.categories.all():
            print '  {}'.format(c.name)

    assert Item.objects.all().count() == 2


def test_item_category():
    """ Factory and Model development driver
    """
    category = CategoryWithItemFactory.create()

    c = ItemCategory.objects.get(id=category.id)
    print '{}'.format(c.name)
    for i in c.items.all():
        print '  {}'.format(i.name)

    assert ItemCategory.objects.get(id=category.id).name == c.name
