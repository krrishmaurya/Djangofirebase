from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('signup',views.Singup.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login')
]