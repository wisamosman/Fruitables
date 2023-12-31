from django.shortcuts import render,redirect
from .models import Profile,Phones,Address
from .forms import SignupForm, ActivateUser
from django.contrib.auth.models import User
from django.views import generic
from fruit.models import Fruit,Review
from django.contrib.admin.views.decorators import staff_member_required



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()

    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})



@staff_member_required
def dashboard(request):
    users = User.objects.all().count()
    fruits = Fruit.objects.all().count()
    reviews = Review.objects.all().count()



    return render(request,'registration/dashboard.html',{
        'users' : users ,  
        'fruits': fruits , 
        'reviews' : reviews ,  
    })    





