from django.shortcuts import render

# Create your views here.
def baabtra_home(request):
    return render(request, 'baabtra/home.html')

def baabtra_jscript(request):
    return render(request, 'baabtra/jscript.html')
    
def baabtra_new(request):
    return render(request, 'baabtra/new.html')

def baabtra_new1(request):
    return render(request, 'baabtra/new1.html')

def baabtra_largest(request):
    return render(request, 'baabtra/largest.html')

def baabtra_largest3(request):
    return render(request, 'baabtra/largest3.html')

def baabtra_sum(request):
    return render(request, 'baabtra/sum.html')

def baabtra_reverse(request):
    return render(request, 'baabtra/reverse.html') 

def baabtra_palindrome(request):
    return render(request, 'baabtra/palindrome.html')

def baabtra_digits(request):
    return render(request, 'baabtra/digits.html')

def baabtra_digits1(request):
    return render(request, 'baabtra/digits.html')

def baabtra_rtriangle(request):
    return render(request, 'baabtra/rtriangle.html')   

def baabtra_mrtriangle(request):
    return render(request, 'baabtra/mrtriangle.html') 

def baabtra_pyramid(request):
    return render(request, 'baabtra/pyramid.html')

def baabtra_inversep(request):
    return render(request, 'baabtra/inversep.html')

def baabtra_new2(request):
    return render(request, 'baabtra/new2.html')

def baabtra_function(request):
    return render(request, 'baabtra/function.html')

def baabtra_dom(request):
    return render(request, 'baabtra/dom.html')                                      

def baabtra_dom1(request):
    return render(request, 'baabtra/dom1.html')     

def baabtra_calculator(request):
    return render(request, 'baabtra/calculator.html')

def baabtra_password(request):
    return render(request, 'baabtra/password.html') 

def baabtra_jquery(request):
    return render(request, 'baabtra/jquery.html')

def baabtra_product(request):
    return render(request, 'baabtra/product.html')

def baabtra_addproduct(request):
    return render(request, 'baabtra/addproduct.html')

def baabtra_viewproduct(request):
    return render(request, 'baabtra/viewproduct.html')

def baabtra_validation(request):
    return render(request, 'baabtra/validation.html')            
