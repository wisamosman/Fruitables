# Generated by Django 5.0 on 2024-01-08 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0006_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]