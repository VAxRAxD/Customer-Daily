from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date, timedelta
from collections import Counter
from itertools import repeat
from App.models import *

@api_view(('GET',))
def salesreport(request):
    enddate = date.today()+timedelta(days=1)
    startdate = enddate-timedelta(days=30)
    orders = Order.objects.all()
    weekly = orders.filter(date_created__range=[startdate, enddate])
    categories = []
    for order in weekly:
        categories.extend(repeat(order.product.category, order.quantity))
    dict = Counter(categories)
    data = []
    for k, v in dict.items():
        data.append({k: v})
    return Response(data)

@api_view(('GET',))
def chickenreport(request):
    enddate = date.today()+timedelta(days=1)
    startdate = enddate-timedelta(days=30)
    orders = Order.objects.all()
    weekly = orders.filter(date_created__range=[startdate, enddate])
    products = []
    for order in weekly:
        if order.product.category == "Chicken":
            products.extend(repeat(order.product.name, order.quantity))
    dict = Counter(products)
    data = []
    for k, v in dict.items():
        data.append({k: v})
    return Response(data)

@api_view(('GET',))
def seafoodreport(request):
    enddate = date.today()+timedelta(days=1)
    startdate = enddate-timedelta(days=30)
    orders = Order.objects.all()
    weekly = orders.filter(date_created__range=[startdate, enddate])
    products = []
    for order in weekly:
        if order.product.category == "Seafood":
            products.extend(repeat(order.product.name, order.quantity))
    dict = Counter(products)
    data = []
    for k, v in dict.items():
        data.append({k: v})
    return Response(data)

@api_view(('GET',))
def muttonreport(request):
    enddate = date.today()+timedelta(days=1)
    startdate = enddate-timedelta(days=30)
    orders = Order.objects.all()
    weekly = orders.filter(date_created__range=[startdate, enddate])
    products = []
    for order in weekly:
        if order.product.category == "Mutton":
            products.extend(repeat(order.product.name, order.quantity))
    dict = Counter(products)
    data = []
    for k, v in dict.items():
        data.append({k: v})
    return Response(data)