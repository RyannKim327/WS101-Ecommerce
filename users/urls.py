from django.urls import path
from .views import * 

urlpatterns = [
    path("", test),
    path("login/", login),
    path("reg/", register)
]
