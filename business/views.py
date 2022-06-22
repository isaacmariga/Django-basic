import re
from django.shortcuts import render, redirect
from .models import Batch, Deaths, ExpenseGroup, Expenses, Revenue, Customers
from .forms import BatchForm, DeathsForm, ExpensesForm, ExpenseGroupForm, RevenueForm, CustomersForm
from django.contrib.auth.decorators import login_required



# Create your views here.



def home(request):
	projects = Batch.get_all() 
	
	return render(request, 'business/home.html',{'projects':projects})


def batch(request, id):
		# Batch queries
	projects = set(Batch.get_all())
	batch = Batch.get_by_id(id)
	purchase_price = Batch.purchase_cost(id)
	expected_revenue = Batch.expected_revenue(id)

# Deaths queries
	deaths = Deaths.death_by_batch(id) 
	death_sum =Deaths.death_sum(id)

# expences queries
	expense_sum = Expenses.expense_sum(id)
	expenses = Expenses.exp_by_batch(id) 
	expense_by_group = Expenses.sum_by_group_amount(id)
	expense_by_group_list = Expenses.sum_by_group_list()

# revenue queries
	revenue_sum = Revenue.total_revenue(id)
	revenue_by_customer_list = Revenue.sum_by_customer_list()
	revenue_by_customer_amount = Revenue.sum_by_customer_amount(id)
	revenue_by_customer_number = Revenue.sum_by_customer_number(id)
	revenue_by_customer_total = Revenue.sum_by_customer_total(id)

	customers = Customers.customers_by_batch(id)

# profit calculation
	real_profit = revenue_sum - expense_sum
 

#  Graph views
# batch graphs
	revenue_labels= ["Expected Revenue", "Actual revenue"]
	revenue_data =[expected_revenue,real_profit ]

# Expenses graphs
# expenses per item
	expense_item_label= []
	expense_item_amount= []
	for expense in expenses:
			expense_item_label.append(str(expense.details))
			expense_item_amount.append(str(expense.amount))

# expenses by group
	expense_group_amount= []

	for expense in expense_by_group:
			expense_group_amount.append(expense)

	for label in expense_by_group_list:
			expense_group_label = label


# Deaths by reason
	death_label= []
	death_amount= []
	for death in deaths:
			death_label.append(str(death.reason))

			death_amount.append(str(death.number))


# revenue by customer
	rev_customer_amount= []
	num_per_customer_amount= []
	total_by_customer_amount= []

	for revenue in revenue_by_customer_amount:
			rev_customer_amount.append(revenue)
	for number in revenue_by_customer_number:
			num_per_customer_amount.append(number)

	for total in revenue_by_customer_total:
			total_by_customer_amount.append(total)

	for label in revenue_by_customer_list:
			revenue_customer_label = label




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
	{'deaths':deaths, 'id':id, 'death_sum':death_sum, 'purchase_price':purchase_price, 'expense_sum':expense_sum, 'label':label,'label2':label2, 'data':data, 'data2':data2,'revenue_sum':revenue_sum, 'real_profit':real_profit, 'batch':batch, 'projects':projects, 'expense_by_group':expense_by_group, 'customers':customers,'expenses':expenses, 'expense_by_group_list':expense_by_group_list, 'revenue_by_customer_list':revenue_by_customer_list, 'revenue_by_customer_amount':revenue_by_customer_amount, 'revenue_by_customer_number':revenue_by_customer_number, 'revenue_by_customer_total':revenue_by_customer_total, 'expected_revenue':expected_revenue, 'revenue_labels':revenue_labels, 'revenue_data':revenue_data, 'expense_item_label':expense_item_label, 'expense_item_amount':expense_item_amount, 'expense_group_label':expense_group_label, 'expense_group_amount':expense_group_amount,'death_label':death_label, 'death_amount':death_amount,'rev_customer_amount':rev_customer_amount,'num_per_customer_amount':num_per_customer_amount, 'total_by_customer_amount':total_by_customer_amount, 'revenue_customer_label':revenue_customer_label})



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
