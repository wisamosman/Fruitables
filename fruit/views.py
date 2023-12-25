from django.shortcuts import render
from django.views import generic
from .models import Fruit,Review




# Create your views here.

class FruitList(generic.ListView):
    model = Fruit
    paginate_by = 8



class FruitDetail(generic.DetailView):
    model = Fruit    
