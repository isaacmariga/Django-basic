from django import forms
<<<<<<< HEAD
from .models import Batch, Deaths, Expenses, Revenue, Customers, ExpenseGroup
=======
from .models import Batch, Deaths, Expenses, Revenue, Customers,UserProfile  
# from bootstrap_datepicker_plus.widgets import DatePickerInput
>>>>>>> ft-main

class BatchForm(forms.ModelForm):
  class Meta:
    model=Batch
    exclude=['user']
<<<<<<< HEAD
=======
    # widgets = { 'start_date' : DatePickerInput(), 'end_date' : DatePickerInput(),}
>>>>>>> ft-main



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
			
