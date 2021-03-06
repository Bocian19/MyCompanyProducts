# Generated by Django 3.0.3 on 2020-03-03 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_products', '0023_auto_20200227_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoria', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name': 'Wizyta', 'verbose_name_plural': 'Wizyty'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Nazwa kategorii'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wedding_products.Category', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost_of_production',
            field=models.FloatField(blank=True, null=True, verbose_name='Koszt zakupu/wyprodukowania'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='suknie', verbose_name='Fotografia'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=64, verbose_name='Nazwa produktu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.FloatField(null=True, verbose_name='Ilość'),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_net_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Cena sprzedaży netto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('szt.', 'sztuki'), ('mm', 'milimetry'), ('m', 'metry')], default='szt.', max_length=4, verbose_name='Jednostka'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='first_name',
            field=models.CharField(blank=True, max_length=64, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='last_name',
            field=models.CharField(max_length=64, null=True, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='Number telefonu'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateTimeField(blank=True, help_text='YYYY-MM-DD HH:MM', null=True, verbose_name='Data wizyty'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(blank=True, verbose_name='Wzrost')),
                ('waist', models.FloatField(blank=True, verbose_name='Talia')),
                ('hips', models.FloatField(blank=True, verbose_name='Obwód bioder')),
                ('breast', models.FloatField(blank=True, verbose_name='Obwód piersi')),
                ('additional_info', models.CharField(blank=True, max_length=200, verbose_name='Dodatkowe informacje')),
                ('order_date', models.DateField(blank=True, verbose_name='Data zamówienia')),
                ('realization_date', models.DateField(blank=True, verbose_name='Data realizacji')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wedding_products.Product')),
            ],
        ),
    ]
