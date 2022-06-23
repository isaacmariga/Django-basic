from django import forms
from .models import Batch, Deaths, Expenses, Revenue, Customers,UserProfile  , ExpenseGroup
# from bootstrap_datepicker_plus.widgets import DatePickerInput

class BatchForm(forms.ModelForm):
  class Meta:
    model=Batch
    exclude=['user']
    # widgets = { 'start_date' : DatePickerInput(), 'end_date' : DatePickerInput(),}



class DeathsForm(forms.ModelForm):
  class Meta:
    model=Deaths
    exclude=['batch']

class ExpensesForm(forms.ModelForm):
  class Meta:
    model=Expenses
    exclude=['batch']
class ExpenseGroupForm(forms.ModelForm):
  class Meta:
    model=ExpenseGroup
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


class UserForm(forms.ModelForm):
  class Meta:
    model = UserProfile    	
    fields=('name', 'email','bio','picture')
			
