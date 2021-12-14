from itertools import repeat
from collections import Counter
from datetime import date, timedelta
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.models import inlineformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from.decorators import *


@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'App/login.html', context)


@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                phone = request.POST['phone']
                address = request.POST['address']
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='Customer')
                user.groups.add(group)
                Customer.objects.create(
                    user=user,
                    name=user.username,
                    email=user.email,
                    phone=phone,
                    address=address,
                )
                messages.success(
                    request, 'Account was created for ' + username)

                return redirect('login')
        context = {'form': form}
        return render(request, 'App/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    if request.method=="POST":
        id=request.POST.get('id')
        order=Order.objects.get(id=id)
        status=request.POST.get('status')
        order.status=status
        order.save()
        return redirect('/')
    else:
        orders = Order.objects.all()
        customers = Customer.objects.all()
        total_customers = customers.count()
        total_orders = orders.count()
        delivered = orders.filter(status='Delivered').count()
        out_for_delivery = orders.filter(status='Out for delivery').count()
        pending = orders.filter(status='Pending').count()
        context = {'orders': orders,
                'customers': customers,
                'total_orders': total_orders,
                'delivered': delivered,
                'pending': pending,
                'total_customers': total_customers,
                'out_for_delivery': out_for_delivery,
                }
        return render(request, "App/home.html", context)


@login_required(login_url='login')
def accountSettings(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            customer.user.email = customer.email
            customer.user.save()
            return redirect('/')
    context = {'form': form, 'customer': customer}
    return render(request, 'App/accounts.html', context=context)


@login_required(login_url='login')
def products(request):
    if request.method=="POST":
        id=request.POST.get('id')
        product=Product.objects.get(id=id)
        name=request.POST.get('name')
        price=request.POST.get('price')
        category=request.POST.get('category')
        weight=request.POST.get('weight')
        description=request.POST.get('desp')
        product.name=name
        product.price=price
        product.weight=weight
        product.category=category
        product.description=description
        product.save()
        return redirect('/products')
    else:
        products = Product.objects.all()
        return render(request, "App/products.html", {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customer': customer, 'orders': orders,
               'order_count': order_count, 'myFilter': myFilter,'id':id}
    return render(request, "App/customer.html", context)


@login_required(login_url='login')
def createOrder(request, id):
    if request.user.is_staff:
        OrderFormSet = inlineformset_factory(
            Customer, Order, fields=('product', 'status', 'quantity'), extra=6)
    else:
        OrderFormSet = inlineformset_factory(
            Customer, Order, fields=('product', 'quantity'), extra=6)
    customer = Customer.objects.get(id=id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'App/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def deleteProduct(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/products')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def deleteCustomer(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def user(request):
    userid = request.user.id
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for delivery').count()
    context = {'orders': orders, 'total_orders': total_orders, 'delivered': delivered,
               'pending': pending, 'customer_id': userid, 'out_for_delivery': out_for_delivery}
    return render(request, 'App/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def sales(request):
    return render(request, 'App/sales.html')