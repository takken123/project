from django.shortcuts import render,get_object_or_404,redirect
from .models import Order,Order_Detail


# Create your views here.
def order(request):
    order=Order.objects.all()
    if 'keyword' in request.GET:
        keyword =request.GET['keyword']
        if keyword:
            order=order.filter(name__icontains=keyword)


    data={
        'order':order,
    }
    
    return render(request,'orders/order.html',data)
def order_detail(request,id):
    detail =get_object_or_404(Order,pk=id)
    data={
        'detail':detail,
    }
    if request.method == 'POST':
        order_id = request.POST['order_id']
        username = request.POST['username']
        email = request.POST['email']
        city= request.POST['city']
        phone = request.POST['phone']
        message = request.POST['message']
        item_name=request.POST['item']
        price=request.POST['price']


        order = Order_Detail(order_id=order_id,email=email,firstname=username,city=city,
                 item_name=item_name,phone=phone,price=price,message=message)
        order.save()
        return redirect('/orders/'+order_id)

    return render(request,'orders/order_detail.html',data)