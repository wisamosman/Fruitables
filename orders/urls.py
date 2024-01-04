from django.urls import path
from .views import add_to_cart, OrderList,chackout_page ,process_payment,payment_failed,payment_success
from fruit.models import Fruit

app_name = "orders"

urlpatterns = [
    path('' , OrderList.as_view()),
    path('add-to-cart' , add_to_cart ,name='add_to_cart'),
    path('checkout' , chackout_page),
    path('checkout/payment' , process_payment),
    path('checkout/payment/success' , payment_success),
    path('checkout/payment/failed' , payment_failed),
    
]