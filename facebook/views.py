from django.shortcuts import render

# Create your views here.

def facebook_home(request):
    return render(request,'facebook_template/home.html')
    

def facebook_home1(request):
    return render(request,'facebook_template/home1.html')

def facebook_management(request):
    return render(request,'facebook_template/management.html')

def facebook_faculty(request):
    return render(request,'facebook_template/faculty.html')

def facebook_about(request):
    return render(request,'facebook_template/about.html') 

def facebook_contact(request):
    return render(request,'facebook_template/contact.html')            

