# -*- coding: utf-8 -*-
import pytest
from sqlalchemy.sql import func
from apps.customer.models import Customer
from apps.item.models import Item
from apps.sale.models import Sale, SaleDetail

pytestmark = pytest.mark.django_db


def test_customer(customer_data):
    """ SQLAlchemy test
    """
    customers = Customer.sa.query(
        Customer.sa.screen_name,
        Customer.sa.sex,
        Customer.sa.birth_day,
    ).filter(
        Customer.sa.sex == 1,
    )
    assert customers.count() != 0


def test_top5_sales_items(sales_data):
    """ get top 5 items in terms of sales
    """
    top_sales_item = SaleDetail.sa.query(
        SaleDetail.sa.item_id.label('item_id'),
        Item.sa.name.label('name'),
        func.sum(SaleDetail.sa.price).label('ttl_sale'),
    ).outerjoin(
        Item.sa, Item.sa.id == SaleDetail.sa.item_id
    ).group_by(
        SaleDetail.sa.item_id
    ).order_by('ttl_sale desc').limit(5)

    assert top_sales_item.count() == 5


def test_top5_ttl_sale_customer(sales_data):
    """ get top 5 customer in terms of sales
    """
    top_sales_customer = Sale.sa.query(
        Sale.sa.customer_id.label('id'),
        Customer.sa.screen_name.label('screen_name'),
        func.sum(Sale.sa.price).label('ttl_sale'),
    ).outerjoin(
        Customer.sa, Sale.sa.customer_id == Customer.sa.id
    ).group_by(
        Customer.sa.id, Customer.sa.screen_name
    ).order_by('ttl_sale desc').limit(5)

    assert top_sales_customer.count() == 5
