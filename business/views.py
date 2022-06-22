from django.shortcuts import render, redirect
from .models import Batch, Deaths, ExpenseGroup, Expenses, Revenue, Customers
from .forms import BatchForm, DeathsForm, ExpensesForm, ExpenseGroupForm, RevenueForm, CustomersForm
from django.contrib.auth.decorators import login_required



# Create your views here.



def home(request):
	projects = Batch.get_all() 
	test = Expenses.group_tot()
	
	return render(request, 'business/home.html',{'projects':projects, 'test':test})


def batch(request, id):
	projects = set(Batch.get_all())
	batch = Batch.get_by_id(id)
	purchase_price = Batch.total_cost(id)

	deaths = Deaths.death_by_batch(id) 
	death_sum =Deaths.death_sum(id)


	expense_sum = Expenses.expense_sum(id)
	expenses = Expenses.exp_by_batch(id) 
	expense_by_group = Expenses.sum_by_group_list(id)


	revenue_sum = Revenue.total_revenue(id)
	customers = Customers.customers_by_batch(id)





	exp_profit = purchase_price - expense_sum
	real_profit = revenue_sum - expense_sum

	label= []
	data =[]

	label2= []
	data2 =[]

	for x in expense_by_group:
			data.append(x)


	queryset = Expenses.objects.order_by('-amount').filter(batch_id = id)
	# queryset2 = ExpenseGroup.objects.filter(batch_id = id)


	for expense in queryset:
		label.append(str(expense.group))

	queryset = Deaths.objects.order_by('-date').filter(batch_id = id)


	for expense in queryset:
		data2.append(expense.number)
		label2.append(str(expense.reason))
	# for expense in queryset2:
		# label.append(expense.group)


	return render(request, 'business/batch.html',
	{'deaths':deaths, 'id':id, 'death_sum':death_sum, 'purchase_price':purchase_price, 'expense_sum':expense_sum, 'exp_profit':exp_profit,'label':label,'label2':label2, 'data':data, 'data2':data2,'revenue_sum':revenue_sum, 'real_profit':real_profit, 'batch':batch, 't_p':t_p ,'projects':projects, 'expense_by_group':expense_by_group, 'customers':customers,'expenses':expenses })



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
