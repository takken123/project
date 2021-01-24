from django.db import models

# Create your models here.
class About(models.Model):
    #name = models.CharField(max_length=200)
    photo =models.ImageField(upload_to='photos/%y/%m/%d/')
    about = models.TextField()


    def __str__(self):

        return self.about
class Item(models.Model):
    item_name=models.CharField(max_length=100)
    price = models.IntegerField()
    item_photo = models.ImageField(upload_to='photos/%y/%m/%d/')

    def __str__(self):
        return self.item_name