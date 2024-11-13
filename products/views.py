from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {
      "categories": [
        "House",
        "Land",
        "Sardines",
        "River",
        "Waterfall",
        ""
      ]
    }
    return render(request, "index.html", ctx)
