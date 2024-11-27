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
    ctx['category'] = category.capitalize()
    ctx['filtered'] = True
    pass

  return render(request, "categories.html", ctx)
