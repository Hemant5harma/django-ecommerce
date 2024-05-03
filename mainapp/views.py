from django.shortcuts import render
from .models import Product

# Create your views here.

def ecommerce(request):
    return render(request,'e-commerce.html')

def loginhandle(request):
    return render(request,'login.html')

def signuphandle(request):
    return render(request,'signup.html')

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')

def men(request):
    data = Product.objects.filter(cateogry="men")
    context = {
        'data':data
    }
    return render(request,'men.html',context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def product(request,id):
    data = Product.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request,'productdescription.html',context)