# Generated by Django 3.2.5 on 2021-07-31 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('address', models.TextField(max_length=200)),
                ('shipping_address', models.TextField(max_length=200)),
            ],
        ),
    ]
