from django.shortcuts import render

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
    return render(request,'men.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def product(request):
    return render(request,'productdescription.html')