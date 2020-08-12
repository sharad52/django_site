from django.shortcuts import render,get_object_or_404

from .models import *

from django.http import HttpResponse


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending,
    }

    return render(request,'accounts/dashboard.html',context)


def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html',{ 'products':products })


def customers(request,pk):
    customer = get_object_or_404(Customer,id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    
    context = {
        'customer':customer,
        'orders':orders,
        'total_orders':total_orders,
    }

    return render(request,'accounts/customers.html',context)


