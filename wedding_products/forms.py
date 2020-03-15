from django import forms
from tempus_dominus.widgets import DatePicker


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='hasło', widget=forms.PasswordInput)


class SearchProductForm(forms.Form):
    product_name = forms.CharField(label='Nazwa produktu')


class SearchVisitForm(forms.Form):
    visit_date = forms.DateField(widget=DatePicker(attrs={'autocomplete': 'off'}), label='')


class SearchCategoryForm(forms.Form):
    name = forms.CharField(label='Nazwa kategorii')