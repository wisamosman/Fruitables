from django.shortcuts import render
from django.views import generic
from .models import Fruit,Review
from django.views import View
from django.core.paginator import Paginator




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
    paginator = Paginator(fruitshop_objects, 3)  # تحديد عدد العناصر في كل صفحة
    page_number = request.GET.get('page')  # استخراج رقم الصفحة الحالية من الطلب
    page_obj = paginator.get_page(page_number)  # الحصول على كائن الصفحة الحالية
    return render(request, 'fruitshop_list.html', {
        'page_obj': page_obj,
        'fruitshop_objects':fruitshop_objects,
        })


class FruitDetail(generic.DetailView):
    model = Fruit    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruit_list'] = Fruit.objects.all()  # Add this line to pass the fruit_list to the template
        context['star_range'] = range(1, 6)  # Precompute the range from 1 to 5
        return context
    
    