from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    ctx = {
      "categories": [
        "Mobiles",
        "Clothes",
        "Cameras",
        "Shoes",
        "Keyboard",
        "Perfume"
      ]
    }
    return render(request, "index.html", ctx)

def addtocart(request, id):
  # product = Product.objects.get(productID=id)
  ctx = {
    # "product": product
  }
  return render(request, "addtocart.html", ctx)
