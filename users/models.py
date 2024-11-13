from django.db import models
from django.forms import PasswordInput

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=25, null=False)
    firstname = models.CharField(max_length=25, null=False)
    middlename = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email} - {self.lastname}, {self.firstname} {self.middlename}"
