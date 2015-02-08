# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.item.models import (
    Item, ItemCategory, ItemCategoryRelation
)


class ItemAdmin(admin.ModelAdmin):
    pass


class ItemCategoryAdmin(admin.ModelAdmin):
    pass


class ItemCategoryRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemCategoryRelation, ItemCategoryRelationAdmin)
