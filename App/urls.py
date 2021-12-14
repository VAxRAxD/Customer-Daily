from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='product'),
    path('customers/<str:id>/',views.customer,name='customer'),
    path('create_order/<str:id>/',views.createOrder,name='create_order'),
    path('delete_customer/<str:id>/', views.deleteCustomer, name="delete_customer"),
    path('delete_product/<str:id>/', views.deleteProduct, name="delete_product"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.user, name="user"),
    path('account/<str:id>/', views.accountSettings, name="account"),
    path('update/<str:id>/', views.accountSettings,name='update'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="App/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="App/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="App/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="App/password_reset_done.html"), name="password_reset_complete"),
    path('sales/',views.sales,name="sales"),
]