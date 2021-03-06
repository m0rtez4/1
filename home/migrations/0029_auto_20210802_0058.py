# Generated by Django 3.2.5 on 2021-08-02 00:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0028_auto_20210802_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='عکس دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_cat',
            field=models.BooleanField(default=False, verbose_name='زیر دسته بندی می باشد / نمی باشد'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='home.category', verbose_name='زیر دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام رنگ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='نظر'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نظر'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='نظر نمایش داده شود / نشود'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_reply',
            field=models.BooleanField(default=False, verbose_name='پاسخ نمایش داده شود / نشود'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product', verbose_name='نظر برای محصول'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='پاسخ به نظر'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery/', verbose_name='عکس های محصول'),
        ),
        migrations.AlterField(
            model_name='images',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام سایز'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='color_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.color', verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='مقدار تخفیف'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='image',
            field=models.ImageField(default=True, upload_to='product/color/', verbose_name='عکس محصول دارای ویژگی'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام محصول دارای ویژگی'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product', verbose_name='اضافه کردن ویژگی برای کدام محصول'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='size_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.size', verbose_name='سایز'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='unit_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت اصلی'),
        ),
    ]
