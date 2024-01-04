from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Order, Cart, CartDetail, OrderDetail
from fruit.models import Fruit
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string
from utils.generate_code import generate_code
from django.conf import settings
import stripe

class OrderList(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset()   # all orders 
        queryset = queryset.filter(user=self.request.user)
        return queryset

def chackout_page(request):
    cart = Cart.objects.get(user=request.user, completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE

    if request.method == 'POST':
        code = request.POST['order_code']
        sub_total = cart.cart_total()
        total = sub_total
        html = render_to_string('include/checkout_table.html', {
            'cart_detail': cart_detail,
            'sub_total': round(sub_total, 2),
            'total': round(total, 2),
            request: request,
            'pub_key': pub_key
        })
        return JsonResponse({'result': html})

    sub_total = cart.cart_total()
    total = sub_total

    return render(request, 'orders/checkout.html', {
        'cart_detail': cart_detail,
        'sub_total': round(sub_total, 2),
        'total': round(total, 2),
        'pub_key': pub_key
    })

def add_to_cart(request):
    # get data frontend 
    fruit = Fruit.objects.get(id=request.POST['fruit_id'])
    quantity = request.POST['quantity']

    # get cart
    cart = Cart.objects.get(user=request.user, completed=False)

    # cart detail 
    cart_detail, created = CartDetail.objects.get_or_create(cart=cart, fruit=fruit)
    cart_detail.quantity = quantity
    cart_detail.price = fruit.price
    cart_detail.total = round(int(quantity) * fruit.price, 2)
    cart_detail.save()

    cart = Cart.objects.get(user=request.user, completed=False)
    detail = CartDetail.objects.filter(cart=cart)

    total = f"{cart.cart_total()}$"

    html = render_to_string('include/base_sidebar.html', {'cart_data': cart, 'cart_detail_data': detail, request: request})
    return JsonResponse({'result': html, 'total': total})

def process_payment(request):
    # create product on stripe : ajax

    cart = Cart.objects.get(user=request.user, completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)

    total = cart.cart_total()

    code = generate_code()
    # Save the generated code to the session
    request.session['generated_code'] = code
    request.session.save()

    stripe.api_key = settings.STRIPE_API_KEY_SECRET

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': code
                    },
                    'unit_amount': int(total * 100)
                },
                'quantity': 1
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/orders/checkout/payment/success',
        cancel_url='http://127.0.0.1:8000/orders/checkout/payment/failed',
    )

    return JsonResponse({'session': checkout_session})

def payment_success(request):
    cart = Cart.objects.get(user=request.user, completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)

    generated_code = request.session.get('generated_code')

    # create order
    new_order = Order.objects.create(user=request.user, code=generated_code)
    for object in cart_detail:
        OrderDetail.objects.create(
            order=new_order,
            fruit=object.fruit,
            price=object.price,
            quantity=object.quantity,
            total=object.total
        )

    cart.completed = True
    cart.save()

    return render(request, 'orders/success.html', {
        'code': generated_code
    })

def payment_failed(request):
    return render(request, 'orders/failed.html', {})