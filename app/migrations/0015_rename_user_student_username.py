# Generated by Django 5.1.1 on 2024-10-02 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_shippingaddress_order_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='username',
        ),
    ]
