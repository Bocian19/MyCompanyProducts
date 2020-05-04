import pytest
from django.contrib.auth.models import User
from django.test import Client
from wedding_products.models import Visit, Product, Category, Order


@pytest.mark.django_db
def test_user_create(user):
    print(User.objects.all().count())
    assert User.objects.get(username='Testowy') == user


class TestUrls:

    @pytest.mark.django_db
    def test_login_url(self):
        c = Client()
        c.login(username='Testowy', password='Testowe123')
        response = c.get('/home/')
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_product_create(self):
        c=Client()
        c.login(username='Testowy', password='Testowe123')
        response = c.post('/add_product/', {'product_name': 'Nowy', 'description': 'Nowy opis',
                                           'cost_of_production': '450', 'selling_net_price': '1990',
                                           'category_id': '1', 'quantity': '3', 'unit':'szt.'})
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_add_order_(self):

        visit = Visit.objects.create(first_name='Natalia', last_name='Nowa', telephone_number='888333777',
                                     visit_date='2011-09-01T13:20:30+03:00')
        category = Category.objects.create(name='Suknie ślubne')
        product = Product.objects.create(product_name='Suknia-testowa', description='super',
                                         cost_of_production='1500.00',
                                         selling_net_price='2899', category=category, quantity='3')
        c = Client()
        c.login(username='Testowy', password='Testowe123')

        response = c.post('/add_order/', {'height':'155', 'waist':'70', 'hips':'90', 'breast':'90',
                                     'additional_info':'No info', 'order_date':'2020-05-05',
                                     'realization_date':'2020-08-10', 'product':product, 'visit':visit})
        assert response.status_code == 302




