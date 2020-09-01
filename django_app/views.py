from django.shortcuts import render,get_object_or_404,redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import CustomerForm,OrderForm,ProductForm
from .filters import OrderFilter

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

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs
    
    context = {
        'customer':customer,
        'orders':orders,
        'total_orders':total_orders,
        'myFilter':myFilter
    }

    return render(request,'accounts/customers.html',context)



def createCustomer(request):
    form = CustomerForm
    if request.method =='POST':
        #print('printing POST',request.POST)
        form=CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context ={'form':form}
    
    return render(request,'accounts/create_customers.html',context)

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=8)
    customer = get_object_or_404(Customer,id=pk)
    #form = OrderForm(initial={'customer':customer})
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        #print('printing POST',request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid:
            formset.save()
            return redirect('/')


    context = {'formset':formset}
    return render (request,'accounts/create_order.html',context)


def updateOrder(request,pk_update):
    order = get_object_or_404(Order,id=pk_update)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/create_order.html',context)


def deleteOrder(request,pk):
    order = get_object_or_404(Order,id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request,'accounts/delete.html',context)

def updateCustomer(request,pk):
    customer = get_object_or_404(Customer,id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'accounts/create_customers.html',context)


def deleteCustomer(request,pk):
    customer = get_object_or_404(Customer,id=pk)
    if request.method =='POST':
        customer.delete()
        return redirect('/')

    context = {'item':customer}

    return render(request,'accounts/delete_customer.html',context)

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect('/')


    context = {'form':form}

    return render(request,'accounts/create_product.html',context)