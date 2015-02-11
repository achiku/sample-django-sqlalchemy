# -*- coding: utf-8 -*-
import pytest
from apps.sale.models import Sale, SaleDetail
from tests.factories.sale import SaleFactory, SaleDetailFactory

pytestmark = pytest.mark.django_db


def test_sale_detail():
    sale = SaleFactory.create()
    SaleDetailFactory.create_batch(2, sale=sale)
    for d in SaleDetail.objects.all():
        print '{} -> {}'.format(d.sale, d)

    assert SaleDetail.objects.all().count() == 2


def test_sale():
    SaleFactory.create()
    assert Sale.objects.all().count() == 1
