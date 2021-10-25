from django.shortcuts import render
from .models import Contact, Product
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    allproducts= Product.objects.all()
    context={
        'allproducts': allproducts

    }
    return render(request, 'home.html',context)

def shopcart(request):
    return render(request, 'index.html')

def products(request):
    allproducts= Product.objects.all()
    context={
        'allproducts': allproducts,

    }
    return render(request, 'products.html',context)

def item(request):
    return render(request, 'productItem.html')

def contact(request):
    if request.method=='POST':
        Name= request.POST['name']
        email= request.POST['email']
        feedback= request.POST['feedback']
        inst= Contact(Name=Name, email=email,feedback= feedback)
        inst.save()

    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
    