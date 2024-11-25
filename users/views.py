from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import User
from .middlewares import *

# Create your views here.

def index(request):
    return redirect("USER:LOGIN") # HttpResponse("<script>location.href='login/'</script>")

def encrypt(pw): 
    a = password(pw)
    return a

def test(request):
    return HttpResponse(decrypt(request.COOKIES.get("userInfo")))

def login(request):
    context = {
        "done": False
    }
    if request.method == "POST":
        users = User.objects.filter(Q(username=request.POST.get("username")) | Q(email=request.POST.get("username")))
        if users:
            users = User.objects.get(Q(username=request.POST.get('username')) | Q(email=request.POST.get("username")))
            if users.password == encrypt(request.POST.get("password")):
                response = redirect("PRODUCTS:INDEX") # HttpResponse(b"<h1>Done</h1>")
                cookie = setCookies(response, "userInfo", users.username)
                if cookie.get("result"):
                    return response
                else:
                    return HttpResponse(f"<h1>Error: {cookie.get('message')}</h1>")
            else:
                context = {
                    "done": True,
                    "msg": "Invalid passwords"
                }
        else:
            context = {
                "done": True,
                "msg": "Account not found"
            }
    # TODO: To create a login catch
    # return render(request, "login.html", context)

    try:
        cookie = request.COOKIES.get("userInfo")
        if cookie:
            # return HttpResponse("<script>location.href='../..'</script>")
            return redirect("PRODUCTS:INDEX")
        else:
            return render(request, "login.html", context)
    except:
        # TODO: To create a basic login session
        context = {
            "done": False
        }
        return render(request, "login.html", context)

def register(request):
    ctx = {
        "name": "Sign up"
    }
    if request.method == "POST":
        data = request.POST
        user = User.objects.filter(Q(username=data.get("username")) | Q(email=data.get("email")))
        if user:
            return render(request, "reg.html", context={"info": "User is already existed"})
        pw = encrypt(request.POST.get("password"))
        if pw == encrypt(request.POST.get("rpw")):
            # TODO: Register account
            usr = User(username=data.get("username"), email=data.get("email"), password=pw)
            usr.save()
            return redirect("PRODUCTS:INDEX")
        else:
            return render(request, "reg.html", context={"info": "Invalid passwords"})
    
    try:
        cookie = request.COOKIES.get("userInfo")
        if cookie:
            return redirect("PRODUCTS:INDEX") # HttpResponse("<script>location.href='../..'</script>")
        else:
            return render(request, "reg.html")
    except:
        return render(request, "reg.html")

def logout(request):
    response = redirect("PRODUCTS:INDEX") # HttpResponse("<script>location.href='../..'</script>")
    response.delete_cookie("userInfo")
    return response

    
