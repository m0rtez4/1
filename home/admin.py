from django.contrib import admin
from  .models import *

class ProductVariantInlines(admin.TabularInline):
    model = Variants

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','image','sub_category')
    list_filter = ('create',)
    prepopulated_fields = {
        'slug':('name',)
    }

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','unit_price','discount','total_price','amount','available')
    list_filter = ('available',)
    list_editable = ('amount','available','discount','unit_price')
    raw_id_fields = ('category',)
    inlines = [ProductVariantInlines]
    prepopulated_fields = {
        'slug': ('sku',)
    }

class VariantAdmin(admin.ModelAdmin):
    list_display = ('name','id')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('name','id')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name','id')



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Variants,VariantAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Color,ColorAdmin)