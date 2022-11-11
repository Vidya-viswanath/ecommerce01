from django.urls import path
from . import views

app_name="baabtra"

urlpatterns=[
     path('home',views.baabtra_home),
     path('jscript',views.baabtra_jscript),
     path('new',views.baabtra_new),
     path('new1',views.baabtra_new1),
     path('largest',views.baabtra_largest),
     path('largest3',views.baabtra_largest3),
     path('sum',views.baabtra_sum),
     path('reverse',views.baabtra_reverse),
     path('palindrome',views.baabtra_palindrome),
     path('digits',views.baabtra_digits),
     path('digits1',views.baabtra_digits1),
     path('rtriangle',views.baabtra_rtriangle),
     path('mrtriangle',views.baabtra_mrtriangle),
     path('pyramid',views.baabtra_pyramid),
     path('inversep',views.baabtra_inversep),
     path('new2',views.baabtra_new2),
     path('function',views.baabtra_function),
     path('dom',views.baabtra_dom),
     path('dom1',views.baabtra_dom1),
     path('calculator',views.baabtra_calculator),
     path('password',views.baabtra_password),
     path('jquery',views.baabtra_jquery),
     path('product',views.baabtra_product,name="product"),
     path('addproduct',views.baabtra_addproduct,name="productdetails"),
     path('viewproduct',views.baabtra_viewproduct,name="viewproduct"),
     path('validation',views.baabtra_validation)
     
]
