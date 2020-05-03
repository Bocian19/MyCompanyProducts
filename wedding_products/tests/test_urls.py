import pytest
from django.contrib.auth.models import User
from django.test import Client


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


