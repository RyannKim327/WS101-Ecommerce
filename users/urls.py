from django.urls import path
from .views import * 

app_name = "USER"

urlpatterns = [
    path("", index, name="USER_INDEX"),
    path("login/", login, name="LOGIN"),
    path("reg/", register, name="REGISTER"),
    path("logout/", logout, name="LOGOUT")
]
