# Generated by Django 5.1.3 on 2024-11-25 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_orders_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
