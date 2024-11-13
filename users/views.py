from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import User
from .middlewares import password

# Create your views here.

def index(request):
    return render(request, "login.html")

def encrypt(pw): 
    a = password(pw)
    return a

def login(request):
    # TODO: To create a basic login session
    if request.method == "POST":
        users = User.objects.get(username=request.POST.get("username"))
        if encrypt(users.password) == encrypt(request.POST.get("password")):
           return HttpResponse("<h1>Done</h1>")
    
    # TODO: To create a login catch
    return render(request, "login.html")

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
            return HttpResponse("<h1>Done</h1>")
        else:
            return HttpResponse("<h1>Invalid passwords</h1>")
    return render(request, "reg.html")
