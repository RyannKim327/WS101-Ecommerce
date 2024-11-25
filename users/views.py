from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import User
from .middlewares import *

# Create your views here.

def index(request):
    return HttpResponse("<script>location.href='login/'</script>")

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
                response = HttpResponse(b"<h1>Done</h1>")
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
            return HttpResponse("<script>location.href='../..'</script>")
        else:
            return render(request, "login.html", context)
    except:
        # TODO: To create a basic login session
        context = {
            "done": False
        }
        return render(request, "login.html", context)

def register(request):
    if request.method == "POST":
        data = request.POST
        user = User.objects.filter(Q(username=data.get("username")) | Q(email=data.get("email")))
        if user:
            return HttpResponse("<h1>Existed</h1>")
        pw = encrypt(request.POST.get("password"))
        if pw == encrypt(request.POST.get("rpw")):
            # TODO: Register account
            usr = User(username=data.get("username"), email=data.get("email"), password=pw)
            usr.save()
            return HttpResponse(b"<h1>Done</h1>")
        else:
            return HttpResponse("<h1>Invalid passwords</h1>")
    
    try:
        cookie = request.COOKIES.get("userInfo")
        if cookie:
            return HttpResponse("<script>location.href='../..'</script>")
        else:
            return render(request, "reg.html")
    except:
        return render(request, "reg.html")


    
