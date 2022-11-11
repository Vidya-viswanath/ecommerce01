from django.urls import path
from . import views
app_name="facebook"
urlpatterns=[

    path('home',views.facebook_home),
    path('home1',views.facebook_home1, name="home"),
    path('management',views.facebook_management, name="manage"),
    path('faculty',views.facebook_faculty, name="fac"),
    path('about',views.facebook_about),
    path('contact',views.facebook_contact, name="cont")


]