# Generated by Django 2.2.6 on 2020-05-21 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Postal',
        ),
        migrations.DeleteModel(
            name='Town',
        ),
    ]