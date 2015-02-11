# -*- coding: utf-8 -*-
import factory
from faker import Factory as FakerFactory
from factory.django import DjangoModelFactory
from apps.customer.models import Customer

faker = FakerFactory.create()


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    screen_name = factory.LazyAttribute(lambda x: faker.user_name())
    sex = factory.Iterator([1, 2])
    birth_day = factory.LazyAttribute(lambda x: faker.date())
