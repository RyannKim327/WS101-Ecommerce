from django.shortcuts import render


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
