# -*- coding: utf-8 -*-
import pytest
from apps.stock.models import Stock, StockHistory
from tests.factories.stock import StockFactory, StockHistoryFactory

pytestmark = pytest.mark.django_db


def test_stock():
    stock = StockFactory.create()
    StockHistoryFactory.create_batch(10, stock=stock)

    for history in Stock.objects.get(id=stock.id).details.all():
        print history

    assert StockHistory.objects.all().count() == 10
