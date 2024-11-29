from django.db import models

# Create your models here.
class Product(models.Model):
  productID = models.AutoField(primary_key=True, unique=True)
  productName = models.CharField(max_length=50, null=False)
  productDescription = models.TextField(null=False)
  manufacturer = models.CharField(max_length=100, null=False)
  productImage = models.ImageField(upload_to="products/")
  productStore = models.CharField(max_length=100, default="")
  category = models.CharField(max_length=100, null=False)
  price = models.IntegerField()
  avail = models.IntegerField(default=0)
  stocks = models.IntegerField(default=0)
  discount = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.productName} - {self.productDescription}"

class Cart(models.Model):
  cartID = models.AutoField(primary_key=True, unique=True)
  productID = models.IntegerField()
  userInfo = models.IntegerField()
  storeID = models.IntegerField(default=1)
  quantity = models.IntegerField(default=1)
  
  def __str__(self):
    return f"{self.cartID} - {self.productID} - {self.userInfo}"

class Order(models.Model):
  orderID = models.AutoField(primary_key=True, unique=True)
  productID = models.IntegerField()
  userInfo = models.IntegerField()
  storeID = models.IntegerField(default=1)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f"{self.orderID} - {self.productID} - {self.userInfo}"
