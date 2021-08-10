import django_filters
from django import forms
from .models import *


class ProductFilter(django_filters.FilterSet):
    CH1={
        ('گران ترین ها','گران ترین ها'),
        ('ارزان ترین ها','ارزان ترین ها'),

    }
    CH2={
        ('پرتخفیف ترین ها','پرتخفیف ترین ها'),
        ('کم تخفیف ترین ها','کم تخفیف ترین ها'),

    }
    CH3={
        ('جدید ترین ها','جدید ترین ها')
    }
    CH4={
        ('مورد علاقه ترین ها','مورد علاقه ترین ها')
    }


    price_1 = django_filters.NumberFilter(field_name='unit_price',lookup_expr='gte')
    price_2 = django_filters.NumberFilter(field_name='unit_price',lookup_expr='lte')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),widget=forms.SelectMultiple)
    price = django_filters.ChoiceFilter(choices=CH1,method='price_filter',widget=forms.Select(attrs={'class':'form-control'}))
    price2 = django_filters.ChoiceFilter(choices=CH2,method='price_filter2',widget=forms.Select(attrs={'class':'form-control'}))
    price3 = django_filters.ChoiceFilter(choices=CH3,method='price_filter3',widget=forms.Select(attrs={'class':'form-control'}))
    price4 = django_filters.ChoiceFilter(choices=CH4,method='price_filter4',widget=forms.Select(attrs={'class':'form-control'}))



    def price_filter(self,queryset,name,value):
        data = '-unit_price' if value == 'گران ترین ها' else 'unit_price'
        return queryset.order_by(data)

    def price_filter2(self,queryset,name,value):
        data = '-discount' if value == 'پرتخفیف ترین ها' else 'discount'
        return queryset.order_by(data)

    def price_filter3(self,queryset,name,value):
        data = '-create' if value == 'جدید ترین ها' else 'create'
        return queryset.order_by(data)

    def price_filter4(self,queryset,name,value):
        data = 'favourite' if value == 'مورد علاقه ترین ها' else '-favourite'
        return queryset.order_by(data)
