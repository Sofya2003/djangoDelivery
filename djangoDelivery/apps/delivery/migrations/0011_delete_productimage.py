# Generated by Django 4.0.4 on 2022-07-10 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_alter_productinbasket_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]