# Generated by Django 3.2.5 on 2021-07-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_myuser_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='postal_code',
            field=models.PositiveIntegerField(blank=True, max_length=10, null=True),
        ),
    ]