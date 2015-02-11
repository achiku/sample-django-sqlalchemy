# -*- coding: utf-8 -*-
import random
import pytest
from sqlalchemy.sql import func
from tests.factories.customer import CustomerFactory
from tests.factories.item import ItemFactory
from tests.factories.sale import SaleFactory, SaleDetailFactory
from apps.customer.models import Customer
from apps.item.models import Item
from apps.sale.models import SaleDetail

pytestmark = pytest.mark.django_db


def test_customer():
    """ SQLAlchemy test
    """
    CustomerFactory.create_batch(10)
    customers = Customer.sa.query(
        Customer.sa.screen_name,
        Customer.sa.sex,
        Customer.sa.birth_day,
    ).filter(
        Customer.sa.sex == 1,
    )
    assert customers.count() != 0


def test_top_sales():
    """ SQLAlchemy test
    """
    items = ItemFactory.create_batch(10)
    for _ in xrange(20):
        sale = SaleFactory.create()
        SaleDetailFactory.create(sale=sale, item=items[random.randint(0, len(items) - 1)])

    top_sales = SaleDetail.sa.query(
        SaleDetail.sa.item_id.label('item_id'),
        Item.sa.name.label('name'),
        func.sum(SaleDetail.sa.price).label('ttl_sale'),
    ).outerjoin(
        Item.sa, Item.sa.id == SaleDetail.sa.item_id
    ).group_by(
        SaleDetail.sa.item_id
    ).order_by('ttl_sale desc').limit(3)

    assert top_sales.count() == 3
