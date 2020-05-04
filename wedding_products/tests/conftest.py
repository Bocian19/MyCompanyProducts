import pytest
from wedding_products.models import Category, Product, Order, Visit
from django.contrib.auth.models import User

@pytest.fixture
def product():
    category = Category.objects.create(name='Suknie ślubne')
    product = Product.objects.create(product_name='Suknia-testowa', description='super', cost_of_production='1500.00',
                                     selling_net_price='2899', category=category, quantity='3' )
    return product

@pytest.fixture
def visit():
    visit = Visit.objects.create(first_name='Natalia', last_name='Nowa', telephone_number='888333777',
                               visit_date='2011-09-01T13:20:30+03:00')
    return visit


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


@pytest.fixture
def user():
    user = User.objects.create_superuser(username='Testowy', password='Testowe123!')
    user.save()
    return user

