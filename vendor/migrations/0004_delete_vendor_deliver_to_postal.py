# Generated by Django 2.2.6 on 2020-05-21 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendordeliverypostal_vendordeliverytown'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vendor_Deliver_To_Postal',
        ),
    ]
