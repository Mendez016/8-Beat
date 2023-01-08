from email.mime import audio
from getpass import getuser
from http.client import HTTPResponse
from django.shortcuts import render
from BEAT.models import usuario,cancion,state
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone as Tz
from django.urls import reverse
import os
def firstOpen(request):
    state.objects.all().delete()
    return HttpResponseRedirect(reverse("BEAT:index"))

def index(request):
    try:
        stat=state.objects.all()[0]
        estado=stat.status
        identificador=stat.pkU
    except:
        estado="F"
        identificador=0
    names=usuario.objects.all()[identificador].nombre
    largo=len(cancion.objects.all())-1
    imagen={}
    user=getuser()
    i=cancion.objects.all()[0]
    imagen=i.Prim.replace("C:","/static/C%3A")+user+i.imagenSec.replace("0.png","")
    return render(request,"BEAT\index.html",{'imagenes':imagen,'estado':estado,'logeado':names,'largo':largo})
def songs(request):
    try:
        stat=state.objects.all()[0]
        estado=stat.status
        identificador=stat.pkU
    except:
        estado="F"
        identificador=0
    names=usuario.objects.all()[identificador].nombre
    imagen=""
    song=""
    user=getuser()
    i=cancion.objects.all()[0]
    imagen=i.Prim.replace("C:","/static/C%3A")+user+i.imagenSec.replace("0.png","")
    song=i.Prim.replace("C:","/static/C%3A")+user+i.audioSec.replace("0.mp3","")

    return render(request,"BEAT\songsPage.html",{'imagenes':imagen,'canciones':song,'largo':
    len(cancion.objects.all()),'logeado':names,'estado':estado})

def registro(request):
    return render(request,"BEAT\sigIn.html")

def ingreso(request):
    return render(request,"BEAT\ingreso.html",{'sts':False})

def add(request):
    return render(request,"BEAT/add.html")

def addNew(request):
    try:
        names=request.POST['nombre']
        track=request.POST['audios']
        icon=request.POST['imagenes']
    except:
        return HttpResponse("Error")
    else:
        strack=str(track)
        simage=str(icon)
        user=getuser()
        ruta=f'C:/Users/{user}/Downloads/'
        Sruta=f'C:/Users/{user}/Documents/miPaginaWeb/PaginaWeb/BEAT/templates/BEAT/static'
        os.rename(ruta+strack,Sruta+'/cancion'+str(len(cancion.objects.all()))+'.mp3')
        os.rename(ruta+simage,Sruta+'/imagen'+str(len(cancion.objects.all()))+'.png')
        rutaSong='/Documents/miPaginaWeb/PaginaWeb/BEAT/templates/BEAT/static'+'/cancion'+str(len(cancion.objects.all()))+'.mp3'
        rutaIcon='/Documents/miPaginaWeb/PaginaWeb/BEAT/templates/BEAT/static'+'/imagen'+str(len(cancion.objects.all()))+'.png'
        newSong=cancion(name=names,Prim='C:/Users/',audioSec=rutaSong,imagenSec=rutaIcon)
        newSong.save()
        return HttpResponseRedirect(reverse("BEAT:musica"))

def hacerRegistro(request):
    try:
        name=request.POST['user']
        passw=request.POST['password']
        register=str(Tz.now()).replace("+00:00","")
    except:
        return HttpResponse("Error")
    else:
        newUser=usuario(
            nombre=name,
            password=passw,
            registro=register
        )
        newUser.save()
        return HttpResponseRedirect(reverse("BEAT:index"))

def LogIn(request):
    try:
        name=request.POST['user']
        passw=request.POST['password']
    except:
        return HttpResponse("Error")
    else:
        for i in usuario.objects.all():
            if(i.nombre==name and i.password==passw):
                newState=state(status="",pkU=i.pk-1)
                newState.save()
                return HttpResponseRedirect(reverse("BEAT:index"))
        newState=state(status="T",pkU=0)
        newState.save()
        return HttpResponseRedirect(reverse("BEAT:errorIn"))

def errorIngreso(request):
    state.objects.all().delete()
    return render(request,"BEAT\ingreso.html",{'sts':True})