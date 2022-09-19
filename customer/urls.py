from django.urls import path
from . import views

urlpatterns=[
    path('home',views.customer_home),
    path('cart',views.customer_cart),
    path('order',views.customer_order),
    path('name',views.customer_name)
]