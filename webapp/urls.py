from django.urls import path , include

from . import views

urlpatterns = [
    path('', views.home), # /college
    path('contact/',views.contact),
    path('login',views.loginpage),
    path('register',views.register)
]