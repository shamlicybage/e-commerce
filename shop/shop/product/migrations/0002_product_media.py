# Generated by Django 2.2.17 on 2021-02-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/products'),
        ),
    ]
