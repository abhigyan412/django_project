from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",  views.index, name='homepage'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name ='contact'),
    path("someone",views.someone, name ='someone'),
    path("login",views.login, name ='login'),
    path("signup",views.signup_view, name ='signup'),
    path("icecream",views.icecreams , name ='icecream'),


]