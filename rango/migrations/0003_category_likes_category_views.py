# Generated by Django 4.1 on 2025-01-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
