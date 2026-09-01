from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path("",views.kidshomepage , name='kids'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('girls/', views.girls , name='girls'),
    path('boys/', views.boys , name='boys'),
    path('cart/', views.cart , name='cart'),
    path('profile/', views.profile, name='profile'),
    path('order/', views.order, name='order'),
    path('logout/', views.logout, name='logout'),
    path('view/', views.view, name='view'),
    # path('plain/', views.plain, name='plain'),
    # path('productviews/', views.productviews, name='productviews'),
]
 