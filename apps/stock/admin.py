# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.stock.models import Stock, StockHistory


class StockAdmin(admin.ModelAdmin):
    pass


class StockHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stock, StockAdmin)
admin.site.register(StockHistory, StockHistoryAdmin)
