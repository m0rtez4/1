from django.contrib import admin
from  .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','image')
    list_filter = ('create',)
    prepopulated_fields = {
        'slug':('name',)
    }

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','unit_price','discount','total_price','amount','available')
    list_filter = ('available',)
    prepopulated_fields = {
        'slug': ('sku',)
    }

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
