# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.sale.models import Sale, SaleDetail


class SaleAdmin(admin.ModelAdmin):
    pass


class SaleDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleDetail, SaleDetailAdmin)
