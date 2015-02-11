# -*- coding: utf-8 -*-
from datetime import datetime
import factory
from factory.django import DjangoModelFactory
from tests.factories.customer import CustomerFactory
from tests.factories.item import ItemFactory
from apps.sale.models import Sale, SaleDetail


class SaleFactory(DjangoModelFactory):
    """ SalesFactory
    """
    class Meta:
        model = Sale

    time = datetime.now()
    price = factory.Iterator([100, 200, 300, 400])
    customer = factory.SubFactory(CustomerFactory)


class SaleDetailFactory(DjangoModelFactory):
    """ SalesFactory
    """
    class Meta:
        model = SaleDetail

    sale = factory.SubFactory(SaleFactory)
    item = factory.SubFactory(ItemFactory)
    price = factory.Iterator([100, 200, 300, 400])
    count = factory.Iterator([1, 2])
