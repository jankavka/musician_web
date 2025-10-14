from django.shortcuts import render
from django.http import HttpResponse, Http404
from web_site.models import Event, Project, Photos

# Create your views here.

def index(request):
    return render(request, "web_site/index.html")

def concerts(request):
    try:
        events_list = Event.objects.all()
    except:
        raise Http404("Events are empty")
    context = {"events_list": events_list}
    return render(request, "web_site/concerts.html", context)

def contact(request):
    return render(request, "web_site/contact.html")

def projects(request):
    return render(request, "web_site/projects.html")

def photos(request):
    try:
        photos_list = Photos.objects.all()
    except:
        raise Http404("Phohots are empty")
    context = {"photos_list":photos_list}
    return render(request, "web_site/photos.html", context)


def videos(request):
    return render(request, "web_site/videos.html")
