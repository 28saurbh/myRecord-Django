from django.db import models
from datetime import datetime, date
# Create your models here.

class Customer(models.Model):
    # customer_sno = models.CharField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=False)

    customer_bill = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=20)
    customer_mobile = models.CharField(max_length=12)
    customer_village = models.CharField(max_length=50)
    customer_paid_bal = models.CharField(max_length=100)
    customer_due_bal = models.CharField(max_length=200)
    customer_total_bal = models.CharField(max_length=20)