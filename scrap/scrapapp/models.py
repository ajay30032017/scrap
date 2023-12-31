from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Customer(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE ,null=True,blank=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=80)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=128 ,null=True)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
            
        except:
            url = ''
        
        return url
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=True)
    Transaction_id = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_total_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def get_total_price(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,null=True,blank=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order,null=True,blank=True,on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def get_total(self):
        total = self.product.price* self.quantity
        
        return total
    
    
class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order,null=True,blank=True,on_delete=models.SET_NULL)
    address = models.CharField(max_length=120,null=True)
    city = models.CharField(max_length=120,null=True)
    state = models.CharField(max_length=120,null=True)
    zipcode = models.CharField(max_length=120,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    


    
class Pickup(models.Model):
    weight = models.IntegerField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    address = models.CharField(max_length=128,null=True,blank=True)
    pincode = models.CharField(max_length=128,null=True,blank=True)
    
    def total_weight(self):
        return self.weight
    
    
    
    
    
    
    
class userTypeModel(models.Model):
    userType = models.CharField(max_length=128)
    user= models.OneToOneField(User,on_delete=models.CASCADE ,null=True,blank=True)
    
    def __str__(self):
        return self.userType
    
    
