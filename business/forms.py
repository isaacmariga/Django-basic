from django import forms
from .models import Batch, Deaths, Expenses, Revenue, Customers


class BatchForm(forms.ModelForm):
  class Meta:
    model=Batch
    exclude=['user']
  



class DeathsForm(forms.ModelForm):
  class Meta:
    model=Deaths
    exclude=['batch']

class ExpensesForm(forms.ModelForm):
  class Meta:
    model=Expenses
    exclude=['batch']

class RevenueForm(forms.ModelForm):
  class Meta:
    model=Revenue
    exclude=['batch']
    Widgets = { 'customer' : forms.CheckboxSelectMultiple() ,}


class CustomersForm(forms.ModelForm):
  class Meta:
    model=Customers
    exclude=['batch']