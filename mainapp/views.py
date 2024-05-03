from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def ecommerce(request):
    return render(request,'e-commerce.html')

def loginhandle(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']

        user = authenticate(username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect('/ecom/')

    return render(request,'login.html')

def signuphandle(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']

        if not uname or not email or not passw:
            messages.error(request, 'All fields are required.')
        elif User.objects.filter(username=uname).first():
            messages.success(request,'Username already taken !!')
        else:
            user = User(username=uname,email=email)
            user.set_password(passw)
            user.save()
            messages.success(request,'account created successfully !!')
            return redirect('/login/') 
            


        
        # return HttpResponse("your account suuccessfully created !!")

    return render(request,'signup.html')

def checkout(request):
    return render(request,'checkout.html')

def logouthandle(request):
    logout(request)
    return redirect('/ecom/')

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