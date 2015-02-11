# -*- coding: utf-8 -*-
import pytest
from tests.factories.customer import CustomerFactory

pytestmark = pytest.mark.django_db


def test_customer():
    """ Factory and Model development driver
    """
    c = CustomerFactory()
    print c

    assert True
