import pytest
from wedding_products.models import Visit, Product, Category, Order
from django.utils import timezone

#test of creating visit
@pytest.mark.django_db
def test_visit_model(visit):
    assert Visit.objects.get(first_name='Natalia') == visit


#test of creating product
@pytest.mark.django_db
def test_product_create(product):
    assert Product.objects.get(product_name='Suknia-testowa') == product


#test of creating order
@pytest.mark.django_db
def test_order_create(order):
    assert Order.objects.get(order_date='2020-05-05') == order