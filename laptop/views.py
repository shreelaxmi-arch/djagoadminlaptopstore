from django.shortcuts import render
from .models import Laptop

# Create your views here.
def index(request):
    laptop_list=Laptop.objects.all()
    return render(request,'index.html',{'laptops':laptop_list})

def about(request):
    laptop_list=Laptop.objects.description
    return render(request,'about.html',{'laptops':laptop_list})