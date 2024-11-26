from django.db import models

# Create your models here.
class Product(models.Model):
    productID = models.AutoField(primary_key=True, unique=True)
    productName = models.CharField(max_length=50, null=False)
    productDescription = models.CharField(max_length=500, null=False)
    manufacturer = models.CharField(max_length=100, null=False)
    # expiryDate = models.DateField()
    img = models.ImageField(upload_to="products/")
    category = models.CharField(max_length=100, null=False)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.productName} - {self.productDescription}"

class Order(models.Model):
    orderID = models.AutoField(primary_key=True, unique=True)
    productID = models.CharField(max_length=1000, null=False)
    userInfo = models.CharField(max_length=25, null=True)
    quantuty = models.IntegerField()

    def __str__(self):
        return f"{self.orderID} - {self.productID} - {self.userInfo}"
