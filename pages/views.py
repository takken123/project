from django.shortcuts import render
from .models import About
from orders.models import Order



# Create your views here.


def home(request):
    item = Order.objects.all()
    data={
        'item':item,


    } 
    return render(request, 'pages/home.html',data)
      



def about(request):
    about =About.objects.all()

    data={
        'about':about,
    }

    return render(request,'pages/about.html',data)