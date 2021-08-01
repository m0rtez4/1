from django.contrib import admin
from .models import *


class ItemInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ['user','product','variant','size','color','quantity','price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','f_name','l_name','phone','address','postal_code2','get_price','paid','detail','send','code']
    list_editable = ['send','code']
    inlines = [ItemInline]

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','start','end','discount','active']



admin.site.register(Order,OrderAdmin)
admin.site.register(ItemOrder)
admin.site.register(Coupon,CouponAdmin)
