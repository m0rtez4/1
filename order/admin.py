from django.contrib import admin
from .models import *


class ItemInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ['user','product','variant','size','color','quantity']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','f_name','l_name','address','phone','postal_code2','paid','detail']
    inlines = [ItemInline]





admin.site.register(Order,OrderAdmin)
admin.site.register(ItemOrder)
