# Generated by Django 3.0.3 on 2020-02-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_products', '0010_auto_20200217_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='selling_final_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
