from django.contrib.auth.models import User
from django.db import models

from store.models import Book


# Create your models here.
class Cart(models.Model):
    books=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    date_added=models.DateField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.books.name


    def subtotal(self):
        return self.quantity*self.books.price

class Account(models.Model):
    Acctnumber = models.CharField(max_length=30)
    Accttype = models.CharField(max_length=30)
    Amount = models.IntegerField()

    def __str__(self):
        return self.Acctnumber

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.CharField(max_length=100)
    order_status=models.CharField(max_length=30,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    noofitems=models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


