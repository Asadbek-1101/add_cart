# Generated by Django 5.0.6 on 2024-06-15 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
