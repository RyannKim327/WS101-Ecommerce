from django.urls import path
from .views import *

app_name = "PRODUCTS"

urlpatterns = [
    path("", index, name="INDEX"),
    path("addtocart/<int:id>", addtocart, name="ADDTOCART"),
    path("addproduct", addproduct, name="ADDPRODUCT"),
    path("category/<str:category>", categories, name="CATEGORY"),
    path("addedtocart/<int:id>", addedtocart, name="ADDEDTOCART"),
    path("carts", viewcarts, name="CARTS"),
    path("deletecart", deletecart, name="DELETECART"),
    path("order", orderfromcart, name="ORDERCART"),
    path("vieworders", vieworders, name="VIEWORDERS")
]
