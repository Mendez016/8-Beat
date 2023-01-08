from ast import arg
from urllib import request
from BEAT import views
from django.urls import path
app_name='BEAT'
urlpatterns = [
    path('index/',views.index,name="index"),
    path('music/',views.songs,name="musica"),
    path('ingreso/',views.ingreso,name="ingreso"),
    path('registro/',views.registro,name="registro"),
    path("hacerRegistro/",views.hacerRegistro,name="hacerRegistro"),
    path("logIn/",views.LogIn,name="logIn"),
    path("add/",views.add,name="add"),
    path("addNew/",views.addNew,name="addNew"),
    path("errorIn/",views.errorIngreso,name="errorIn"),
    path("",views.firstOpen,name="fOpen")
]