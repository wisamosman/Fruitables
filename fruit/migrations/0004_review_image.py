# Generated by Django 5.0 on 2023-12-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0003_alter_fruit_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(default=1, upload_to='review'),
            preserve_default=False,
        ),
    ]
