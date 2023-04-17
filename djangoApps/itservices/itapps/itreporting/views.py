from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Home Page'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'})

def products(request):
    return render(request, 'itreporting/products.html', {'title': 'Products'})

def profile(request):
    return render(request, 'itreporting/profile.html', {'title': 'Profile'})

