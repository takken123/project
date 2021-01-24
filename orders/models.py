from django.db import models

# Create your models here.
class Order(models.Model):
    name =models.CharField(max_length=100)
    photo=models.ImageField(upload_to='photos/%y/%m/%d/')
    price =models.IntegerField()

    def __str__(self):
        return self.name


class Order_Detail(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('delivered','Delivered'))
    item_name = models.CharField(max_length=100)
    order_id=models.IntegerField()
    price=models.IntegerField()
    firstname=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    message=models.TextField()
    email=models.EmailField(max_length=100)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    def __str__(self):
        return self.email
