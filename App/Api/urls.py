from django.urls import path
from . import views

urlpatterns = [
    path('chicken_sales_report/',views.chickenreport,name="chicken_report"),
    path('seafood_sales_report/',views.seafoodreport,name="seafood_report"),
    path('mutton_sales_report/',views.muttonreport,name="mutton_report"),
    path('sales_report/',views.salesreport,name="sales_report"),
]