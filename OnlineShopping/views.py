from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")