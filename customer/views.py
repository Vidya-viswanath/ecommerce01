from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer_template/home.html')

def customer_cart(request):
    return render(request,'customer_template/cart.html')

def customer_order(request):
    return render(request,'customer_template/order.html')

def customer_name(request):
    return render(request, 'customer_template/name.html')
