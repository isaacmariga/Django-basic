from django.db import models
from django.db.models import Avg, Sum

# Create your models here.
class Batch(models.Model):
	purchased = models.IntegerField()
	unit_price = models.IntegerField()
	projected_SP = models.IntegerField()
	start_date = models.DateTimeField(auto_now_add=False)
	end_date = models.DateTimeField(auto_now_add=False)

	def __str__(self):
		return str(self.id)

	def get_all():
		result = Batch.objects.all()
		return result
	
	def total_cost(id):
			u_p = list(Batch.objects.filter(id=id).aggregate(Sum('unit_price')).values())
			u_p = int("".join(map(str,u_p)))
			
			purch = list(Batch.objects.filter(id=id).aggregate(Sum('purchased')).values())
			purch = int("".join(map(str,purch)))
			cost = u_p * purch
			return cost


class Deaths(models.Model):
	number = models.IntegerField()
	reason = models.TextField(max_length=300)
	date = models.DateTimeField(auto_now_add=False)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)

	@classmethod
	def ind_by_batch(cls, id):
		result = Deaths.objects.filter(batch = id)
		return result

	@classmethod
	def death_sum(cls, id):
			table = list(Deaths.objects.filter(batch_id=id).aggregate(Sum('number')).values())
			test = all( i == None for i in table)
			if (test) == True:
					return 1
			else:
					table = int("".join(map(str,table)))
					return table



class Expenses(models.Model):
	amount = models.IntegerField()
	expense = models.CharField(max_length=30)
	details = models.TextField(max_length=300)
	date = models.DateTimeField(auto_now_add=False)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)


	def __str__(self):
		return str(self.id)


	@classmethod
	def expense_sum(cls, id):
			table = list(Expenses.objects.filter(batch_id=id).aggregate(Sum('amount')).values())
			test = all( i == None for i in table)
			if (test) == True:
					return 1
			else:
					table = int("".join(map(str,table)))
					return table
					

class Revenue(models.Model):
	SP = models.IntegerField()
	number = models.IntegerField()
	date = models.DateTimeField(auto_now_add=False)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)


# def profit():
class Editors(models.Model):
    editor_name = models.CharField(max_length=200)
    num_users = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.editor_name, self.num_users)