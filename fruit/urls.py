from django.urls import path
from .views import FruitList,FruitDetail, Fruit1List

app_name = 'fruit'

urlpatterns = [
    path('',FruitList.as_view(),name='fruit_list'),
    path('',Fruit1List.as_view(),name='fruit1_list'),
    path('<slug:slug>',FruitDetail.as_view(),name='fruit_detail'),
]