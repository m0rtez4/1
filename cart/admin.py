from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('user','product','variant','quantity',)
    list_filter = ('user','product')


admin.site.register(Cart,CartAdmin)
