from django.shortcuts import render 
from django.http import HttpResponse
from .models import *


# Create your views here.
def kidshomepage(request):
    products_views = Product_view.objects.all()
    return render(request , 'kids/index.html',{'products_views': products_views})

def about(request):
    return render(request , 'kids/about.html')

def girls(request):
    girls = Girl.objects.all()
    return render(request , 'kids/girls.html',{'girls': girls})

def boys(request):
    boys = Boy.objects.all()
    return render(request , 'kids/boys.html',{'boys': boys})

def cart(request):
    return render(request , 'kids/cart.html')

def profile(request):
    return render(request , 'kids/profile.html')
    
def order(request):
    return render(request , 'kids/order.html')

def logout(request):
    return render(request , 'kids/logout.html')

def contact(request):
    return render(request , 'kids/contact.html')

def view(request):
    products = Product.objects.all()
    return render(request , 'kids/view.html',{'products': products})

# def plain(request):
#     products = Product.objects.all()
#     return render(request , 'kids/plain.html' , {'products': products})
