from django.urls import path 
from .views import signup , dashboard

app_name = 'accounts'

urlpatterns = [
    path('signup' , signup),
    path('dashboard' , dashboard),
    
]