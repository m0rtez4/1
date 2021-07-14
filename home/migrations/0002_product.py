# Generated by Django 3.2.5 on 2021-07-12 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('amount', models.PositiveIntegerField()),
                ('unit_price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('total_price', models.PositiveIntegerField()),
                ('information1', models.TextField()),
                ('information2', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product')),
                ('sku', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
