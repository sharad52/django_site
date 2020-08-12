from django.urls import path
from .views import home,products,customers

app_name='django_app'

urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('customers/<str:pk>/',customers,name='customers'),
]