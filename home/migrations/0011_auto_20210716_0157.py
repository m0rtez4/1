# Generated by Django 3.2.5 on 2021-07-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210715_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='variants',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variants',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variants',
            name='unit_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
