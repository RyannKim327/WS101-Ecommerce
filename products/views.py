from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from users.middlewares import decrypt, checker

from users.models import User


# Create your views here.
def index(request):
    cookie = ""
    total = 0
    totalorders = 0
    if checker(request):
        return redirect("USER:PROFILE")
    try:
        cookie = decrypt(request.COOKIES.get("userInfo"))
        user = User.objects.get(username=cookie)
        crts = Cart.objects.filter(userInfo=user.userID)
        orders = Order.objects.filter(userInfo=user.userID)
        total = len(crts)
        totalorders = len(orders)
    except:
        pass
    products = Product.objects.all()[:10]
    ctx = {
        "categories": [
            "Mobiles",
            "Clothes",
            "Cameras",
            "Shoes",
            "Keyboard",
            "Perfume",
        ],
        "cookie": cookie,
        "products": products,
        "total": total,
        "totalorders": totalorders,
    }
    return render(request, "index.html", ctx)


def addtocart(request, id):
    if checker(request):
        return redirect("USER:PROFILE")
    try:
        cookie = request.COOKIES.get("userInfo")
        users = User.objects.get(username=decrypt(cookie))
        totalorders = len(Order.objects.filter(userInfo=users.userID))
        ctx = {"cookie": decrypt(cookie), "totalorders": totalorders}

        try:
            prod = Product.objects.filter(productID=id)
            if prod:
                product = Product.objects.get(productID=id)
                ctx["product"] = product
            else:
                ctx["valid"] = "There is no data existed"

        except:
            pass

        return render(request, "addtocart.html", ctx)
    except Exception as e:
        print(e)
        # TODO: To redirect to user's login for login and registration
        return HttpResponse(
            "<script>alert('You need to login first');location.href='../../user/'</script>"
        )


def addproduct(request):
    if request.method == "POST" and request.FILES["product-image"]:
        # form = ProductImage(request.POST, request.FILES)
        # if form.is_valid():
        #   form.save()
        #   img = form.instance()
        categories = ["Mobiles", "Clothes", "Cameras", "Shoes", "Keyboard", "Perfume"]
        data = request.POST
        product = Product(
            productName=data.get("product-name"),
            productDescription=data.get("product-description"),
            manufacturer=data.get("manufacturer"),
            price=data.get("price"),
            productImage=request.FILES["product-image"],
            category=categories[int(data.get("category")) % len(categories)],
        )
        product.save()

        return render(request, "addproduct.html", {"success": "Product Added"})
        pass
    ctx = {
        "categories": [
            {"id": 0, "name": "Mobiles"},
            {"id": 1, "name": "Clothes"},
            {"id": 2, "name": "Cameras"},
            {"id": 3, "name": "Shoes"},
            {"id": 4, "name": "Keyboard"},
            {"id": 5, "name": "Perfume"},
        ]
    }
    return render(request, "addproduct.html", ctx)


def categories(request, category):
    categories = ["Mobiles", "Clothes", "Cameras", "Shoes", "Keyboard", "Perfume"]

    total = 0
    totalorders = 0
    data = request.COOKIES.get("userInfo")
    ctx = {"filtered": False, "category_lists": categories}

    if data:
        ctx["cookie"] = decrypt(data)
        user = User.objects.get(username=decrypt(data))
        crts = Cart.objects.filter(userInfo=user.userID)
        orders = Order.objects.filter(userInfo=user.userID)
        total = len(crts)
        totalorders = len(orders)

    if category.capitalize() in categories:
        products = Product.objects.filter(category=category.capitalize())
        ctx["data"] = products
        # ctx['discounted'] = products.price - (products.price / products.discount)
        ctx["category"] = category.capitalize()
        ctx["filtered"] = True
        ctx["total"] = total
        ctx["totalorders"] = totalorders
    return render(request, "categories.html", ctx)


def addedtocart(request, id):
    if checker(request):
        return redirect("USER:PROFILE")
    try:
        ctx = {}
        cookie = decrypt(request.COOKIES.get("userInfo"))
        user = User.objects.get(username=cookie)
        # product = Product.object.get(productID=id)
        cart = Cart(productID=id, userInfo=user.userID)
        cart.save()
    except Exception as e:
        print(e)
        pass
    return redirect("PRODUCTS:CARTS")


def viewcarts(request):
    if checker(request):
        return redirect("USER:PROFILE")
    try:
        cookie = decrypt(request.COOKIES.get("userInfo"))
        user = User.objects.get(username=cookie)
        ctx = {}
        crts = Cart.objects.filter(userInfo=user.userID)
        totalorders = len(Order.objects.filter(userInfo=user.userID))
        carts = []

        for cart in crts:
            prod = Product.objects.get(productID=cart.productID)
            cost = prod.price
            if prod.discount > 0:
                cost = prod.price - (prod.price / prod.discount)

            carts.append({"cartID": cart.cartID, "product": prod, "cost": cost})
        ctx["cookie"] = cookie
        ctx["products"] = carts
        ctx["total"] = len(crts)
        ctx["totalorders"] = totalorders
        return render(request, "carts.html", ctx)
    except Exception as e:
        print(e)
    return redirect("PRODUCTS:INDEX")


def deletecart(request):
    if checker(request):
        return redirect("USER:PROFILE")
    try:
        data = request.GET.get("data").split(",")
        cookie = decrypt(request.COOKIES.get("userInfo"))
        user = User.objects.get(username=cookie)

        for info in data:
            id = int(info)
            prod = Cart.objects.get(cartID=id)

            if user.userID == prod.userInfo:
                prod.delete()
        return redirect("PRODUCTS:ORDERCART")
    except:
        pass
    # return HttpResponse("Error")
    return redirect("PRODUCTS:INDEX")


def orderfromcart(request):
    if checker(request):
        return redirect("USER:PROFILE")
    try:
        data = request.GET.get("data").split(",")
        cookie = decrypt(request.COOKIES.get("userInfo"))
        user = User.objects.get(username=cookie)

        for info in data:
            id = int(info)
            prod = Cart.objects.get(cartID=id)

            if user.userID == prod.userInfo:
                Order(
                    productID=prod.productID,
                    userInfo=user.userID,
                    storeID=prod.storeID,
                    quantity=prod.quantity,
                    location="",
                ).save()
                prod.delete()
        return redirect("PRODUCTS:VIEWORDERS")
    except Exception as e:
        print(e)
        pass
    return redirect("PRODUCTS:INDEX")


def vieworders(request):
    if checker(request):
        return redirect("USER:PROFILE")
    try:
        checker(request)
        cookie = decrypt(request.COOKIES.get("userInfo"))
        user = User.objects.get(username=cookie)
        ctx = {}
        orders = Order.objects.filter(userInfo=user.userID)
        carts = []
        status = ["pending", "shipping", "packaging", "delivery"]

        for order in orders:
            prod = Product.objects.get(productID=order.productID)
            cost = prod.price
            if prod.discount > 0:
                cost = prod.price - (prod.price / prod.discount)

            print(status[order.status])
            carts.append({
                "orderID": order.orderID,
                "product": prod,
                "cost": cost,
                "location": order.location,
                "status": status[order.status],
            })
        ctx["cookie"] = cookie
        ctx["products"] = carts
        ctx["total"] = len(orders)
        ctx["totalorders"] = len(orders)
        ctx["user"] = user
        return render(request, "orders.html", ctx)
    except Exception as e:
        print(e)
    return redirect("PRODUCTS:INDEX")
