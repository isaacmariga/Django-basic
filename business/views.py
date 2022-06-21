from django.shortcuts import render, redirect
from .models import Batch, Deaths, ExpenseGroup, Expenses, Revenue, Customers
from .forms import BatchForm, DeathsForm, ExpensesForm, ExpenseGroupForm, RevenueForm, CustomersForm
from django.contrib.auth.decorators import login_required



# Create your views here.



def home(request):
	projects = Batch.get_all() 
	
	return render(request, 'business/home.html',{'projects':projects})

def test(request, id , group):
	projects = Batch.get_all() 

	t_s = Expenses.total_search(id, group)
	t_p = Expenses.search(id, group)
	
	return render(request, 'business/test.html',{'t_p':t_p , 'projects':projects, 't_s':t_s})

def batch(request, id):
	deaths = Deaths.ind_by_batch(id) 
	d_sum =Deaths.death_sum(id)
	b_p = Batch.total_cost(id)
	t_e = Expenses.expense_sum(id)
	rev = Revenue.total_revenue(id)
	batch = Batch.get_by_id(id)
	projects = set(Batch.get_all())
	# t_s = Expenses.total_search(id, group)
 
	total = Expenses.expense_sum_per(id)
	t_e = Expenses.expense_sum(id)
	t_p = Expenses.objects.all()
	# a_e = Expenses.objects.filter(id=id).filter(group=group)


	exp_profit = b_p - t_e
	real_profit = rev - t_e

	label= []
	data =[]

	queryset = Expenses.objects.order_by('-amount').filter(batch_id = id)
	# queryset2 = ExpenseGroup.objects.filter(batch_id = id)


	for expense in queryset:
		data.append(expense.amount)
		label.append(expense.details)
	# for expense in queryset2:
		# label.append(expense.group)


	return render(request, 'business/batch.html',
	{'deaths':deaths, 'id':id, 'd_sum':d_sum, 'b_p':b_p, 't_e':t_e, 'exp_profit':exp_profit,'label':label, 'data':data, 'rev':rev, 'real_profit':real_profit, 'batch':batch, 't_p':t_p ,'projects':projects, 'total':total})



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
def new_death(request, id):
	batch = Batch.get_by_id(id)
	current_user = request.user			
	if request.method == 'POST':
		form = DeathsForm(request.POST)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.batch = batch
			name.save()
		return redirect( 'batch', batch.id )
	else:
		form = DeathsForm()
			
	return render(request, 'business/new_death.html', {'form': form, 'batch':batch})



@login_required(login_url='/accounts/login/')
def new_customer(request, id):
	batch = Batch.get_by_id(id)
	current_user = request.user			
	if request.method == 'POST':
		form = CustomersForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.batch = batch
			name.save()
		return redirect( 'batch', batch.id )
	else:
		form = CustomersForm()
			
	return render(request, 'business/new_customer.html', {'form': form, 'batch':batch})



@login_required(login_url='/accounts/login/')
def new_expense(request, id):
	batch = Batch.get_by_id(id)
	current_user = request.user			
	if request.method == 'POST':
		# form2 = ExpenseGroupForm(request.POST)
		form = ExpensesForm(request.POST)

		if form.is_valid():
			# name2 = form.save(commit=False)
			name = form.save(commit=False)
			name.user = current_user
			name.batch = batch
			name.save()
			# name2.save()
		return redirect( 'batch', batch.id)
	else:
		form = ExpensesForm()
		form2 = ExpenseGroupForm()
			
	return render(request, 'business/new_expense.html', {'form': form, 'form2': form2 ,'batch':batch})


	
@login_required(login_url='/accounts/login/')
def new_revenue(request, id):
	batch = Batch.get_by_id(id)
	current_user = request.user			
	if request.method == 'POST':
		form = RevenueForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = current_user
			name.batch = batch
			name.save()
		return redirect( 'batch', batch.id )
	else:
		form = RevenueForm()
			
	return render(request, 'business/new_revenue.html', {'form': form, 'batch':batch})
