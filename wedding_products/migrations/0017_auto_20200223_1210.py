# Generated by Django 3.0.3 on 2020-02-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_products', '0016_auto_20200223_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='dresses/'),
        ),
    ]
