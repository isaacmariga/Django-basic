from django.shortcuts import render, redirect
from .models import Batch, Deaths, Expenses, Revenue, Customers
from .forms import BatchForm, DeathsForm, ExpensesForm, RevenueForm, CustomersForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def about(request):
  
  return render(request, 'about/about.html', )

def landing(request):
  
  return render(request, 'landing/landing.html', )




def home(request):
	projects = Batch.get_all() 

	return render(request, 'business/home.html',{'projects':projects})



def batch(request, id):
	deaths = Deaths.ind_by_batch(id) 
	d_sum =Deaths.death_sum(id)
	b_p = Batch.total_cost(id)
	t_e = Expenses.expense_sum(id)
	rev = Revenue.total_revenue(id)
	exp_profit = b_p - t_e
	real_profit = rev - t_e

	label= []
	data =[]

	queryset = Expenses.objects.order_by('-amount').filter(batch_id = id)
	for expense in queryset:
		data.append(expense.amount)
		label.append(expense.expense)


	return render(request, 'business/batch.html',
	{'deaths':deaths, 'id':id, 'd_sum':d_sum, 'b_p':b_p, 't_e':t_e, 'exp_profit':exp_profit,'label':label, 'data':data, 'rev':rev, 'real_profit':real_profit})


def charts(request):
	label= []
	data =[]

	queryset = Expenses.objects.order_by('-amount')
	for expense in queryset:
		data.append(expense.amount)
		label.append(expense.expense)
	return render(request, 'business/charts.html',{'labels':label, 'data':data }) 



@login_required(login_url='/accounts/login/')
def new_batch(request):
	current_user = request.user			
	if request.method == 'POST':
		form = BatchForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.save()
		return redirect( 'home' )
	else:
		form = BatchForm()
			
	return render(request, 'business/new_batch.html', {'form': form})



@login_required(login_url='/accounts/login/')
def new_death(request):
	batch = Batch.get_by_id(id)
	current_user = request.user			
	if request.method == 'POST':
		form = DeathsForm(request.POST)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.batch = batch
			name.save()
		return redirect( 'home' )
	else:
		form = DeathsForm()
			
	return render(request, 'business/new_death.html', {'form': form})



@login_required(login_url='/accounts/login/')
def new_customer(request):
	current_user = request.user			
	if request.method == 'POST':
		form = CustomersForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.save()
		return redirect( 'home' )
	else:
		form = CustomersForm()
			
	return render(request, 'business/new_customer.html', {'form': form})



@login_required(login_url='/accounts/login/')
def new_expense(request):
	current_user = request.user			
	if request.method == 'POST':
		form = ExpensesForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.save()
		return redirect( 'home' )
	else:
		form = ExpensesForm()
			
	return render(request, 'business/new_expense.html', {'form': form})


	
@login_required(login_url='/accounts/login/')
def new_revenue(request):
	current_user = request.user			
	if request.method == 'POST':
		form = RevenueForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.save()
		return redirect( 'home' )
	else:
		form = RevenueForm()
			
	return render(request, 'business/new_revenue.html', {'form': form})
