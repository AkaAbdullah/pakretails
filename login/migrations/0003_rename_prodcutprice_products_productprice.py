# Generated by Django 3.2.5 on 2021-08-01 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prodcutprice',
            new_name='productprice',
        ),
    ]
