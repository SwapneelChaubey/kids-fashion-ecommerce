from django.shortcuts import render 
from django.http import HttpResponse
from .models import *


# Create your views here.
def kidshomepage(request):
    return render(request , "kids/index.html")

def about(request):
    return render(request , 'kids/about.html')

def girls(request):
    return render(request , 'kids/girls.html')

def boys(request):
    return render(request , 'kids/boys.html')

def cart(request):
    return render(request , 'kids/cart.html')

def profile(request):
    return render(request , 'kids/profile.html')
    
def order(request):
    return render(request , 'kids/order.html')

def logout(request):
    return render(request , 'kids/logout.html')

def productviews(request):
    return HttpResponse("this is product views")

def contact(request):
    return render(request , 'kids/contact.html')

def view(request):
    products = Product.objects.all()
    return render(request , 'kids/view.html',{'productss': products})

# def plain(request):
#     products = Product.objects.all()
#     return render(request , 'kids/plain.html' , {'products': products})
