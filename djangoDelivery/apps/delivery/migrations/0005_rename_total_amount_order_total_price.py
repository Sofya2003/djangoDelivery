# Generated by Django 4.0.4 on 2022-07-05 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_alter_product_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]
