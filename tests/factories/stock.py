# -*- coding: utf-8 -*-
from datetime import datetime
import factory
from faker import Factory as FakerFactory
from factory.django import DjangoModelFactory
from tests.factories.item import ItemFactory
from apps.stock.models import Stock, StockHistory

faker = FakerFactory.create()


class StockFactory(DjangoModelFactory):
    """ SalesFactory
    """
    class Meta:
        model = Stock

    item = factory.SubFactory(ItemFactory)
    count = faker.random_digit()


class StockHistoryFactory(DjangoModelFactory):
    """ SalesFactory
    """
    class Meta:
        model = StockHistory

    time = datetime.now()
    stock = factory.SubFactory(StockFactory)
    item = factory.SubFactory(ItemFactory)
    count = faker.random_digit()
