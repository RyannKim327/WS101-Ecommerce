from django.db import models

# Create your models here.
class Product(models.Model):
    productID = models.AutoField(primary_key=True, unique=True)
    productName = models.CharField(max_length=50, null=False)
    manufacturer = models.CharField(max_length=100, null=False)
    # expiryDate = models.DateField()
    category = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.productName} - {self.expiryDate}"
