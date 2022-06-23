from django.contrib import admin
<<<<<<< HEAD
from .models import Batch, Deaths, ExpenseGroup, Expenses, Revenue, Customers
=======
from .models import Batch, Deaths, Expenses, Revenue, Customers,UserProfile
>>>>>>> ft-main
# Register your models here.



admin.site.register(Batch)
admin.site.register(Deaths)
admin.site.register(Expenses)
<<<<<<< HEAD
admin.site.register(Revenue)
admin.site.register(Customers)
admin.site.register(ExpenseGroup)
=======
admin.site.register(Revenue, RevenueAdmin)
admin.site.register(Customers)
admin.site.register(UserProfile)
>>>>>>> ft-main
