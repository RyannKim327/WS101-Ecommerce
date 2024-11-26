from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .middlewares import *
from .forms import *

# Create your views here.
def index(request):
  cookie = ""
  try:
    cookie = decrypt(request.COOKIES.get("userInfo"))
  except:
     pass
  ctx = {
    "categories": [
      "Mobiles",
      "Clothes",
      "Cameras",
      "Shoes",
      "Keyboard",
      "Perfume"
    ],
    "cookie": cookie
  }
  return render(request, "index.html", ctx)

def addtocart(request, id):
  try:
    # cookie = request.COOKIE.get("user")
    try:
      product = Product.objects.get(productID=id)
      ctx = {
        "product": product
      }
    except:
      ctx = {}
    return render(request, "addtocart.html", ctx)
  except:
    # TODO: To redirect to user's login for login and registration
    return HttpResponse("<script>alert('You need to login first');location.href='../../user/'</script>")

def addproduct(request):
  if request.method == "POST":
    form = ProductImage(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      img = form.instance()
      return HttpResponse("Done")
    pass
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
  return render(request, "addproduct.html", ctx)

