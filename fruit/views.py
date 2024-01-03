from django.shortcuts import render
from django.views import generic
from .models import Fruit,Review
from django.views import View




# Create your views here.

class FruitList(generic.ListView):
    model = Fruit
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_review'] = Review.objects.all()
        return context

def fruitshop_list(request):
    fruitshop_objects = Fruit.objects.all()[:9]
    return render(request,'fruitshop_list.html',{'fruitshop_objects':fruitshop_objects})





class FruitDetail(generic.DetailView):
    model = Fruit    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruit_list'] = Fruit.objects.all()  # Add this line to pass the fruit_list to the template
        context['star_range'] = range(1, 6)  # Precompute the range from 1 to 5
        return context
    
    