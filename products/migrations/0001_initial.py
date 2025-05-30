# Generated by Django 5.1.3 on 2024-11-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('productName', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=100)),
                ('expiryDate', models.DateField()),
            ],
        ),
    ]
