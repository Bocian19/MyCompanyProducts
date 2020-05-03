import pytest
from wedding_products.models import Visit, Product, Category
from django.utils import timezone


@pytest.fixture
def visit():
    visit = Visit.objects.create(first_name='Natalia', last_name='Nowa', telephone_number='888333777',
                               visit_date='2011-09-01T13:20:30+03:00')
    return visit

#test of creating visit
@pytest.mark.django_db
def test_visit_model(visit):
    assert Visit.objects.get(first_name='Natalia') == visit


@pytest.fixture
def product():
    category = Category.objects.create(name='Suknie ślubne')
    product = Product.objects.create(product_name='Suknia-testowa', description='super', cost_of_production='1500.00',
                                     selling_net_price='2899', category=category, quantity='3' )
    return product


#test of creating product
@pytest.mark.django_db
def test_product_create(product):
    assert Product.objects.get(product_name='Suknia-testowa') == product