from django.db import models


class Profile(models.Model):
    firstname= models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    phone_no= models.IntegerField()
    address = models.TextField(max_length=200)
    shipping_address = models.TextField(max_length=200)
    
    def __str__(self):
        return self.firstname

class Products(models.Model):
    productname = models.CharField(max_length=200)
    productdescription =  models.TextField(max_length=500)
    productprice = models.IntegerField()
    productimage = models.ImageField(upload_to="uploads/")