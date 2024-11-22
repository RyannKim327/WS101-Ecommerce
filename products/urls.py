from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("addtocart/<int:id>", addtocart)
]
