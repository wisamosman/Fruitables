from django.urls import path
from .views import FruitList,FruitDetail

app_name = 'fruit'

urlpatterns = [
    path('',FruitList.as_view(),name='fruit_list'),
    path('<int:pk>',FruitDetail.as_view(),name='fruit_detail'),
]