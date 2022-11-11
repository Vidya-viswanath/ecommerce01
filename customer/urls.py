from django.urls import path
from . import views
app_name="customer"
urlpatterns=[
    path('home',views.customer_home, name='approve'),
    path('cart',views.customer_cart),
    path('order',views.customer_order, name='orders'),
    path('name',views.customer_name),
    path('home1',views.customer_home1),
    path('box',views.customer_box),
    path('box1',views.customer_box1),
    path('box2',views.customer_box2),
    path('box3',views.customer_box3),
    path('flex',views.customer_flex),
    path('bootstrap',views.customer_bootstrap),
    path('response',views.customer_response)
]