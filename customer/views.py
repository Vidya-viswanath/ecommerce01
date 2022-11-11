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

def customer_home1(request):
    return render(request, 'customer_template/home1.html')
    
def customer_box(request):
    return render(request, 'customer_template/box.html')

def customer_box1(request):
    return render(request, 'customer_template/box1.html')

def customer_box2(request):
    return render(request, 'customer_template/box2.html' )

def customer_box3(request):
    return render(request, 'customer_template/box3.html')

def customer_flex(request):
    return render(request, 'customer_template/flex.html')

def customer_bootstrap(request):
    return render(request, 'customer_template/bootstrap.html')

def customer_response(request):
    return render(request, 'customer_template/response.html')
