# Generated by Django 3.2.5 on 2021-08-02 00:31

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0027_product_favourite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'رنگ', 'verbose_name_plural': 'رنگ ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'عکس', 'verbose_name_plural': 'عکس ها'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'سایز', 'verbose_name_plural': 'سایزها'},
        ),
        migrations.AlterModelOptions(
            name='variants',
            options={'verbose_name': 'ویژگی', 'verbose_name_plural': 'ویژگی ها'},
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='تعداد محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='موجود / ناموجود'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='home.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریح ثیت محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='مقدار تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='fa_user', to=settings.AUTH_USER_MODEL, verbose_name='مورد علاقه ی کاربران'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product', verbose_name='عکس محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='information1',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات کوتاه محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='information2',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات تکمیلی محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='آدرس url'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('None', 'none'), ('Size', 'size'), ('Color', 'color'), ('Both', 'Both')], max_length=200, null=True, verbose_name='وضعیت ویژگی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت اصلی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین بروزرسانی'),
        ),
    ]
