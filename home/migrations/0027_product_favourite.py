# Generated by Django 3.2.5 on 2021-08-01 04:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0026_alter_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='fa_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
