# Generated by Django 3.2.5 on 2021-08-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210801_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id_cart',
            field=models.PositiveIntegerField(blank=True, default=1000, null=True),
        ),
    ]
