# Generated by Django 5.0 on 2023-12-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0004_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
