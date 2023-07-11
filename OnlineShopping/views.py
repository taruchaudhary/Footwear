from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# from django.contrib import messages

def homepage(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def addtowishlist(request):
    return render(request,"add-to-wishlist.html")

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")

def men(request):
    return render(request,"men.html")

def orderComplete(request):
    return render(request,"order-complete.html")

def productdetail(request):
    return render(request,"product-detail.html")

def women(request):
    return render(request,"women.html")

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user = authenticate(request,username=username, password=password)
        if user is not None: 
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1 !=pass2:
            return HttpResponse("Confirm Password not same")
        else:
            my_user= User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request,"register.html")

def logout (request):
    logout(request)
    return redirect("login")