from django.shortcuts import render, redirect
from .models import Customer
from myapp2.form import CustomerForm
# Create your views here.


def home(request):
    customer = Customer.objects.all
    return render(request, 'home.html', {'customer': customer})


def add_customer(request):
    form = CustomerForm
    return render(request, 'add_customer.html', {'form': form})


def add(request):
    form = CustomerForm(request.POST)
    form.save()
    return redirect("/home")


def edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'edit.html', {'customer': customer})


def update(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    form.save()
    return redirect("/home")


def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/home')


def search(request):
    given_name = request.POST['name']
    employee = Customer.objects.filter(customer_name__icontains=given_name)
    return render(request, 'show.html', {'customer': employee})
