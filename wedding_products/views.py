import csv

from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum, F
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from tempus_dominus.widgets import DatePicker


from .forms import LoginForm, SearchProductForm, SearchVisitForm, SearchCategoryForm
from .models import Product, Category, Visit, Order


# Create your views here.


class LoginView(View):

    def get(self, request):
        form = LoginForm
        return render(request, 'base.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['username']
            password = form.cleaned_data['password']
            logging_user = authenticate(username=user_login, password=password)
            if logging_user is not None:
                login(request, logging_user)
                return redirect(reverse_lazy('home'))
            else:
                response = "Błędne dane logowania"
                return render(request, 'base.html', {'form': form,
                                                           'response': response})


class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'home.html')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))


class ProductsView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):

        products = Product.objects.annotate(
            final_cost=F('quantity') * F('cost_of_production'))
        summary = products.aggregate(Sum('final_cost'))
        return render(request, 'products.html', {"products": products, "summary": summary})

    def post(self, request):
        form = SearchProductForm(request.POST)
        if form.is_valid():
            products = Product.objects.filter(
                product_name__icontains=form.cleaned_data['product_name']
            )
            return render(request, 'products.html', {"products": products})


class ProductView(View):

    def get(self, request, pk):

        product = Product.objects.get(pk=pk)
        return render(request, 'product.html', {"product": product})


class ProductCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Product
    fields = ['product_name', 'description', 'quantity', 'unit', 'cost_of_production', 'selling_net_price','photo', 'category']
    success_url = reverse_lazy("products")


class OrderView(LoginRequiredMixin, View):
    login_url = '/login/'
    success_url = reverse_lazy('orders')

    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'orders.html', {'orders': orders})


class OrderCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Order
    success_url = reverse_lazy('orders')
    fields = ['height', 'waist', 'hips', 'breast', 'additional_info', 'order_date', 'realization_date', 'product']

    def get_form(self, form_class=None):
        form = super(OrderCreate, self).get_form(form_class)
        form.fields['realization_date'].widget = DatePicker()
        return form


class ProductDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Product
    success_url = reverse_lazy("products")


class ProductUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Product
    fields = ['product_name', 'description', 'quantity', 'unit', 'cost_of_production', 'selling_net_price', 'photo', 'category']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("products")


class CategoryCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Category
    fields = ['name']
    success_url = reverse_lazy("categories")


def create_csv(request):

    products = Product.objects.annotate(
        final_cost=F('quantity') * F('cost_of_production'))
    summary = products.aggregate(Sum('final_cost'))
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="remanent.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['Nazwa produktu', 'Ilość', 'Jednostka', 'Cena cetto', 'Kategoria'])
    for product in products:
        writer.writerow([product.product_name, product.quantity, product.unit, product.cost_of_production,
                         product.category])
    writer.writerow(['Wartosć netto', '', '', summary['final_cost__sum']])

    return response


class VisitsView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):

        visits = Visit.objects.all().order_by('visit_date')
        return render(request, 'visits.html', {"visits": visits})

    def post(self, request):
        form = SearchVisitForm(request.POST)
        if form.is_valid():
            visits = Visit.objects.filter(
                visit_date__icontains=form.cleaned_data['visit_date']
            )
            return render(request, 'visits.html', {"visits": visits})


class VisitCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Visit
    fields = ['first_name', 'last_name', 'telephone_number', 'visit_date']
    success_url = reverse_lazy('visits')


class VisitUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Visit
    fields = ['first_name', 'last_name', 'telephone_number', 'visit_date']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("visits")


class VisitDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Visit
    fields = ['first name', 'last_name', 'telephone_number', 'visit_date', 'visit_create_date']
    success_url = reverse_lazy("visits")


class CategoriesView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):

        categories = Category.objects.all()
        products = Product.objects.all()
        return render(request, 'categories.html', {"categories": categories, "products": products})

    def post(self, request):
        form = SearchCategoryForm(request.POST)
        if form.is_valid():
            category = Category.objects.filter(
                name__icontains=form.cleaned_data['name']
            )
            products = Product.objects.all()
            return render(request, 'categories.html', {"category": category, "products": products})