# Generated by Django 3.2.5 on 2021-08-02 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_order_paid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'کوپن', 'verbose_name_plural': 'کوپن ها'},
        ),
        migrations.AlterModelOptions(
            name='itemorder',
            options={'verbose_name': 'سبد سفارش', 'verbose_name_plural': 'سبدهای سفارشات'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارشات'},
        ),
    ]