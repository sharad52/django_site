from django.urls import path
from .views import home,products,customers,createCustomer,createOrder,updateOrder,deleteOrder,updateCustomer,deleteCustomer,createProduct


app_name='django_app'

urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('customers/<str:pk>/',customers,name='customers'),
    path('createCustomer/',createCustomer,name="createCustomer"),
    path('createOrder/<int:pk>/',createOrder,name='createOrder'),
    path('updateOrder/<int:pk_update>/',updateOrder,name='updateOrder'),
    path('deleteOrder/<int:pk>/',deleteOrder,name='deleteOrder'),
    path('updateCustomer/<int:pk>/',updateCustomer,name='updateCustomer'),
    path('deleteCustomer/<str:pk>/',deleteCustomer,name='deleteCustomer'),
    path('createProduct/',createProduct,name='createProduct'),
]