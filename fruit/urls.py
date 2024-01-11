from django.urls import path
from .views import FruitList,FruitDetail,fruitshop_list
from .api import fruit_list_api,FruitDetailAPI

app_name = 'fruit'

urlpatterns = [
    path('',FruitList.as_view(),name='fruit_list'),
    path('fruitshop_list/',fruitshop_list),
    path('<slug:slug>',FruitDetail.as_view(),name='fruit_detail'),
    path('api/list',fruit_list_api),
    path('api/list/<int:pk>',FruitDetail.as_view()),
]