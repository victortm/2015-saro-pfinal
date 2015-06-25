#!/usr/local/bin/python
#-*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from models import activitie, myacc
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context, RequestContext
from bs4 import BeautifulSoup
import urllib
import datetime

# Create your views here.

# Events storage
xml = urllib.urlopen("http://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=206974-0-agenda-eventos-culturales-100&mgmtid=6c0b6d01df986410VgnVCM2000000c205a0aRCRD")
content = xml.read()
soup = BeautifulSoup(content)
eventdicc = soup.find_all("contenido")

events = activitie.objects.all()
if not events:
    for event in eventdicc:
        title = event.find(nombre="TITULO").string
        cost = event.find(nombre="GRATUITO").string
        date = event.find(nombre="FECHA-EVENTO").string
        date = date.split(" ")[0]
        time = event.find(nombre="HORA-EVENTO").string
        id = event.find(nombre="ID-EVENTO").string
        try:
            moreinfo = soup.find(nombre="CONTENT-URL-ACTIVIDAD").string
            longlength = event.find(nombre="EVENTO-LARGA-DURACION").string
            kind = event.find(nombre="TIPO").string
            kind = kind.split("/")[3] 
        except AttributeError:
            longlength = "Info. no disponible, lo sentimos"
            kind = "Info. no disponible, lo sentimos"
            moreinfo = "Info. no disponible, lo sentimos"
        if longlength == "1":
            longlength = True
        else:
            longlength = False
        if cost == "1":
            cost = "GRATUITO"
        else:
            cost = "NO GRATUITO"
       
        newentry = activitie(title=title, date=date, time=time, 
                              moreinfo=moreinfo, cost=cost, kind=kind,
                              longlength=longlength, id=id)
        newentry.save()


@csrf_exempt
def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")

def index(request):
    events = activitie.objects.all()
    events = activitie.objects.order_by('-date')
    events = events[0:10]
    users = User.objects.all()
    for usr in users:
        name = usr.username
        newuser = myacc(name=name)
        newuser.save()
    ctx = {"events": events,
           "users": users}
        
    return render_to_response('content/index.html', ctx, 
                               context_instance=RequestContext(request))    


def all(request):
    events = activitie.objects.all()
    users = User.objects.all()
    usrname = request.user.username
    ctx = {'events': events,
           'users': users}
    if request.method == "POST":
        rbody = request.body.split("&")
        rqst = rbody[1]
        rqst = rqst.split("=")[1]
        print rqst
        if rqst == "Filter":
            filtby = request.body.split("&")[1]
            filtby = filtby.split("=")[1]
            if filtby == "date":
                events = activitie.objects.order_by('-date')
        else:
            eventid = request.body.split("&")[1]
            eventid = eventid.split("=")[0]
            event = activitie.objects.get(id=eventid)
            pickdate = datetime.date.today() 
            event.pickdate = pickdate
            event.save()
            print usrname
            usracc = myacc.objects.get(name=usrname)
            print usracc
            newentry = usracc.activity.add(event)
      
    return render_to_response('content/all_events.html', ctx, 
                               context_instance=RequestContext(request))


def help(request):
    if request.method =="GET":
        title = "Ayuda"
        users = User.objects.all()
        ctx = {"title": title,
               "users": users}
        return render_to_response('content/help_content.html', ctx, 
                                   context_instance=RequestContext(request))

def user(request,resource):
    users = User.objects.all()
    usrname = resource
    usracc = myacc.objects.get(name=usrname)
    myevents = usracc.activity.all()

    ctx = {'myevents': myevents,
           'users': users}
    return render_to_response('content/myuser.html', ctx, 
                               context_instance=RequestContext(request))
			    

def event(request,resource):
    title = activitie.objects.get(id= resource).title
    date = activitie.objects.get(id= resource).date
    time = activitie.objects.get(id= resource).time
    longlength = activitie.objects.get(id = resource).longlength
    cost = activitie.objects.get(id = resource).cost
    if longlength == True:
        longlength = "Si"
    else:
        longlength = "No"
    ctx = {'title': title,
           'date': date,
           'time': time,
           'longlength': longlength,
           'cost':cost}               
    return render_to_response('content/event_content.html', ctx, 
                               context_instance=RequestContext(request))

def update(request):
    xml = urllib.urlopen("http://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=206974-0-agenda-eventos-culturales-100&mgmtid=6c0b6d01df986410VgnVCM2000000c205a0aRCRD")
    content = xml.read()
    soup = BeautifulSoup(content)
    eventdicc = soup.find_all("contenido")
    for event in eventdicc:
        title = event.find(nombre="TITULO").string
        cost = event.find(nombre="GRATUITO").string
        date = event.find(nombre="FECHA-EVENTO").string
        date = date.split(" ")[0]
        time = event.find(nombre="HORA-EVENTO").string
        id = event.find(nombre="ID-EVENTO").string
        try:
            moreinfo = event.find(nombre="CONTENT-URL-ACTIVIDAD").string
            longlength = event.find(nombre="EVENTO-LARGA-DURACION").string
            kind = event.find(nombre="TIPO").string
            kind = kind.split("/")[3] 
        except AttributeError:
            moreinfo = "Info. no disponible, lo sentimos"
            longlength = "Info. no disponible, lo sentimos"
            kind = "Info. no disponible, lo sentimos"
        if length == "1":
            longlength = True
        else:
            longlength = False
        if cost == "1":
            cost = "GRATUITO"
        else:
            cost = "NO GRATUITO"
        try:
            newentry = activitie.objects.get(id=id)
        except:
            newentry = activitie(title=title, date=date, time=time, 
                                 longlength=longlength, cost=cost, 
                                 moreinfo=moreinfo, id=id)
            newentry.save()
    return HttpResponseRedirect("todas")


def rss(request,resource):
    usrname = request.user.username
    usracc = myacc.objects.get(name=usrname)
    usrevents = usracc.activity.all()
    ctx = {'usrname': usrname,
           'events': usrevents}
    return render_to_response('rss/user.rss', ctx, 
                               context_instance=RequestContext(request))

# Funcionalidad optativa
# Canal RSS de la página principal
def indexrss(request):
    events = activitie.objects.all()
    events = activitie.objects.order_by('-date')
    events = events[0:10]
    ctx = {'events': events} 
    return render_to_response('rss/index.rss', ctx, 
                               context_instance=RequestContext(request))



# Error terminal -- USO DE: context_instance=RequestContext(request)
#/usr/local/lib/python2.7/dist-packages/Django-1.7.6-py2.7.egg/django/template/defaulttags.py:63: UserWarning: A {% csrf_token %} was used in a template, but the context did not provide the value.  This is usually caused by not using RequestContext.
#  warnings.warn("A {% csrf_token %} was used in a template, but the context did not provide the value.  This is usually caused by not using RequestContext.")
