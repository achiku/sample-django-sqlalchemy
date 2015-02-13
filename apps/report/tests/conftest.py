# -*- coding: utf-8 -*-
import random
import pytest
from tests.factories.customer import CustomerFactory
from tests.factories.item import ItemFactory
from tests.factories.sale import SaleFactory, SaleDetailFactory


@pytest.fixture()
def sales_data():
    items = ItemFactory.create_batch(10)
    sales = []
    for _ in xrange(20):
        sale = SaleFactory.create()
        SaleDetailFactory.create(sale=sale, item=items[random.randint(0, len(items) - 1)])
        sales.append(sale)
    return sales


@pytest.fixture()
def customer_data():
    return CustomerFactory.create_batch(10)
