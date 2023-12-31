from django.shortcuts import render
from django.views import generic
from .models import Company
from fruit.models import Fruit , Review




def home(request):
    fruits = Fruit.objects.all()[:8]
    reviews = Review.objects.all()
    return render(request,'settings/home.html',{

        'fruits':fruits,
        'reviews':reviews,
    })

# Create your views here.

class CompanyList(generic.ListView):
    model = Company

