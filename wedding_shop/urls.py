"""wedding_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from wedding_products.views import LoginView, HomeView, UserLogoutView, ProductsView, ProductCreate, ProductDelete, ProductUpdate, CategoryCreate, \
    create_csv, VisitsView, VisitCreate, VisitUpdate, VisitDelete, CategoriesView, ProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('products/', ProductsView.as_view(), name='products'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('add_product/', ProductCreate.as_view(), name='add-product'),
    path('add_category/', CategoryCreate.as_view(), name='add-category'),
    path('delete_product/<pk>', ProductDelete.as_view(), name='delete-product'),
    path('update_product/<pk>', ProductUpdate.as_view(), name='update-product'),
    path('product/<pk>', ProductView.as_view(), name='product'),
    path('create-csv/', create_csv, name='create-csv'),
    path('visits/', VisitsView.as_view(), name='visits'),
    path('add_visit/', VisitCreate.as_view(), name='add-visits'),
    path('update_visits/<pk>', VisitUpdate.as_view(), name='update-visits'),
    path('delete_visits/<pk>', VisitDelete.as_view(), name='delete-visits'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
