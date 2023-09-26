from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cart
from .models import Account, Order
from .models import Book


@login_required
def add_cart(request,b):
    book=Book.objects.get(id=b)
    user=request.user
    try:
        cart=Cart.objects.get(books=book,user=user)
        if cart.quantity<cart.books.stock:
            cart.quantity+=1
        cart.save()

    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,books=book,quantity=1)
        cart.save()
    return redirect('cart:cartview')

def cartview(request):
    total=0
    user=request.user
    try:
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity*i.books.price
    except Cart.DoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart,'total':total})
@login_required()
def cart_remove(request,b):
    book=Book.objects.get(id=b)
    user=request.user
    try:
        cart=Cart.objects.get(books=book,user=user)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()
        else:
            cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')

def delete_cart(request,b):
    book = Book.objects.get(id=b)
    user = request.user
    try:
        cart = Cart.objects.get(books=book, user=user)
        cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')
@login_required()
def orderform(request):
    total=0
    if(request.method=="POST"):
        a = request.POST['a']
        p = request.POST['p']
        c = request.POST['c']
        u=request.user
        cart=Cart.objects.filter(user=u)
        for i in cart:
           total+=i.quantity*i.books.price
           account=Account.objects.get(Acctnumber=c)
        if (account.Amount >= total):
             account.Amount= account.Amount - total
             account.save()

             for i in cart:
                 o=Order.objects.create(user=u,books=i.books,address=a,phone=p,order_status="paid",delivery_status="pending",noofitems=i.quantity)
                 i.books.stock=i.books.stock-i.quantity
                 i.save()
                 o.save()
             cart.delete()
             msg="Ordered Successfully"
             return render(request, 'orderdetails.html',{'msg':msg,'total':total})
        else:
            msg="Insufficient Amount. You cannot place order"
            return render(request, 'orderform.html')

    return render(request,'orderform.html')

@login_required()
def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u,order_status="paid")
    return render(request,'orderview.html',{'o':o,'name':u.username})