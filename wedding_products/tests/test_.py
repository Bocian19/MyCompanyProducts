import pytest
from wedding_products.models import Visit, Product, Category, Order
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


@pytest.fixture
def order():
    visit = Visit.objects.create(first_name='Natalia', last_name='Nowa', telephone_number='888333777',
                                 visit_date='2011-09-01T13:20:30+03:00')
    category = Category.objects.create(name='Suknie ślubne')
    product = Product.objects.create(product_name='Suknia-testowa', description='super', cost_of_production='1500.00',
                                     selling_net_price='2899', category=category, quantity='3')
    order = Order.objects.create(height='155', waist='70', hips='90', breast='90',
                                 additional_info='No info', order_date='2020-05-05',
                                 realization_date='2020-08-10', product=product, visit=visit)
    return order

#test of creating order
@pytest.mark.django_db
def test_order_create(order):
    assert Order.objects.get(order_date='2020-05-05') == order