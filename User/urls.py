from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('advisor/',views.advisor),
    path('booking/',views.booking),
    path('adminlogin/',views.admin),
    path('add/',views.add),
]
 