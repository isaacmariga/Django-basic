from re import L
from django.shortcuts import render
from django.shortcuts import render
from .models import Batch, Deaths, Expenses, Revenue

# Create your views here.



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