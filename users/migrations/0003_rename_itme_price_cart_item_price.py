# Generated by Django 4.0 on 2021-12-27 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='itme_price',
            new_name='item_price',
        ),
    ]
