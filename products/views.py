from sys import exception
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .middlewares import *
from .forms import *

from users.models import User

# Create your views here.
def index(request):
  cookie = ""
  try:
    cookie = decrypt(request.COOKIES.get("userInfo"))
  except:
    pass
  products = Product.objects.all()
  print(products)
  ctx = {
    "categories": [
      "Mobiles",
      "Clothes",
      "Cameras",
      "Shoes",
      "Keyboard",
      "Perfume"
    ],
    "cookie": cookie,
    "products": products
  }
  return render(request, "index.html", ctx)

def addtocart(request, id):
  try:
    cookie = request.COOKIES.get("userInfo")
    ctx = {
      "cookie": decrypt(cookie)
    }
    
    try:
      prod = Product.objects.filter(productID=id)
      if prod:
        product = Product.objects.get(productID=id)
        ctx['product'] = product
      else:
        ctx['valid'] = "There is no data existed"
    
    except:
      pass

    return render(request, "addtocart.html", ctx)
  except Exception as e:
    print(e)
    # TODO: To redirect to user's login for login and registration
    return HttpResponse("<script>alert('You need to login first');location.href='../../user/'</script>")

def addproduct(request):
  if request.method == "POST" and request.FILES['product-image']:
    # form = ProductImage(request.POST, request.FILES)
    # if form.is_valid():
    #   form.save()
    #   img = form.instance()
    categories = [
      "Mobiles",
      "Clothes",
      "Cameras",
      "Shoes",
      "Keyboard",
      "Perfume"
    ]
    data = request.POST
    product = Product(
      productName = data.get("product-name"),
      productDescription = data.get("product-description"),
      manufacturer = data.get("manufacturer"),
      price = data.get("price"),
      productImage = request.FILES["product-image"],
      category = categories[int(data.get("category")) % len(categories)]
    )
    product.save()

    return render(request, "addproduct.html", {'success': 'Product Added'})
    pass
  ctx = {
    "categories": [
      {
        "id": 0,
        "name": "Mobiles"
      },
      {
        "id": 1,
        "name": "Clothes"
      },
      {
        "id": 2,
        "name": "Cameras"
      },
      {
        "id": 3,
        "name": "Shoes"
      },
      {
        "id": 4,
        "name": "Keyboard"
      },
      {
        "id": 5,
        "name": "Perfume"
      }
    ]
  }
  return render(request, "addproduct.html", ctx)

def categories(request, category):
  categories = [
      "Mobiles",
      "Clothes",
      "Cameras",
      "Shoes",
      "Keyboard",
      "Perfume"
  ]
  
  data = request.COOKIES.get("userInfo")
  ctx = {
    "filtered": False,
    "category_lists": categories
  }
  
  if(data):
    ctx['cookie'] = decrypt(data)
  
  if category.capitalize() in categories:
    products = Product.objects.filter(category=category.capitalize())
    ctx['data'] = products
    # ctx['discounted'] = products.price - (products.price / products.discount)
    ctx['category'] = category.capitalize()
    ctx['filtered'] = True
    pass

  return render(request, "categories.html", ctx)

def addedtocart(request, id):
  try:
    ctx = {}
    cookie = decrypt(request.COOKIES.get("userInfo"))
    user = User.objects.get(username=cookie)
    # product = Product.object.get(productID=id)
    cart = Cart(
      productID = id,
      userInfo = user.userID
    )
    cart.save()
  except Exception as e:
    print(e)
    pass
  return redirect("PRODUCTS:CARTS")

def viewcarts(request):
  cookie = decrypt(request.COOKIES.get("userInfo"))
  user = User.objects.get(username=cookie)
  ctx = {}
  crts = Cart.objects.filter(userInfo=user.userID)
  carts = []

  for cart in crts:
    prod = Product.objects.get(productID=cart.productID)
    cost = prod.price
    if prod.discount > 0:
      cost = prod.price - (prod.price / prod.discount)

    carts.append({
      "cartID": cart.cartID,
      "product": prod,
      "cost": cost
    })
  ctx['products'] = carts
  ctx['total'] = len(crts)
  return render(request, "carts.html", ctx)

def deletecart(request):
  if request.method == "POST":
    data = request.POST.carts
    for info in data:
      id = info.orderID
      Product.objects.get(orderID=id).delete()
  return {
    "done": True
  }
