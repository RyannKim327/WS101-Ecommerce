from django.urls import path
from .views import *

app_name = "PRODUCTS"

urlpatterns = [
    path("", index, name="INDEX"),
    path("addtocart/<int:id>", addtocart, name="ADDTOCART")
]
