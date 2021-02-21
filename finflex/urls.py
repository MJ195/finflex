from django.urls import path
from . views import *

urlpatterns=[

path("",home.as_view(),name="home"),
path("form",form.as_view(),name="form"),
path("register",user_registeration,name="register"),
path("login",user_login,name="login"),
path("logout",user_logout,name="logout"),
path("booking",my_booking,name="booking"),
path("delete/<pk>",delete_booking,name="delete"),
path("profile",profile,name="profile")
]