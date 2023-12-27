from django.shortcuts import render
from django.views import generic
from .models import Fruit,Review




# Create your views here.

class FruitList(generic.ListView):
    model = Fruit
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_review'] = Review.objects.all()
        return context

    



class FruitDetail(generic.DetailView):
    model = Fruit    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruit_list'] = Fruit.objects.all()  # Add this line to pass the fruit_list to the template
        return context
