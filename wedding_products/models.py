from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa kategorii")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Product(models.Model):

    SZTUKI = 'szt.'
    MILIMETRY = 'mm'
    METRY = "m"

    UNIT_CHOICES = [
        (SZTUKI, 'sztuki'),
        (MILIMETRY, 'milimetry'),
        (METRY, 'metry'),
    ]

    product_name = models.CharField(max_length=64, blank=True, verbose_name="Nazwa produktu")
    quantity = models.FloatField(null=True, verbose_name="Ilość")
    unit = models.CharField(choices=UNIT_CHOICES, null=False, max_length=4, default=SZTUKI, verbose_name="Jednostka")
    description = models.TextField(null=True, blank=True, verbose_name="Opis")
    cost_of_production = models.FloatField(null=True, blank=True, verbose_name="Koszt zakupu/wyprodukowania")
    selling_net_price = models.FloatField(null=True, blank=True, verbose_name="Cena sprzedaży netto")
    photo = models.ImageField(null=True, blank=True, upload_to='suknie', verbose_name="Fotografia")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Kategoria")

    def price_for_the_clients(self):
        if self.selling_net_price:
            return self.selling_net_price*1.23

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"


class Visit(models.Model):
    first_name = models.CharField(max_length=64, blank=True, verbose_name="Imię")
    last_name = models.CharField(max_length=64, null=True, verbose_name="Nazwisko")
    telephone_number = models.CharField(max_length=15, blank=True, verbose_name="Number telefonu")
    visit_date = models.DateTimeField(null=True, blank=True, verbose_name="Data wizyty")
    visit_create_date = models.DateTimeField(auto_now_add=True, help_text='When the visit was created')

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.first_name, self.first_name, self.telephone_number, self.visit_date, self.visit_create_date)

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"


class Order(models.Model):
    height = models.FloatField(blank=True, verbose_name="Wzrost")
    waist = models.FloatField(blank=True, verbose_name="Talia")
    hips = models.FloatField(blank=True, verbose_name="Obwód bioder")
    breast = models.FloatField(blank=True, verbose_name="Obwód piersi")
    additional_info = models.CharField(max_length=200, blank=True, verbose_name="Dodatkowe informacje")
    order_date = models.DateField(blank=True, verbose_name="Data zamówienia")
    realization_date = models.DateField(blank=True, verbose_name="Data realizacji")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    visit = models.ForeignKey(Visit, on_delete=models.PROTECT, blank=True, null=True)







