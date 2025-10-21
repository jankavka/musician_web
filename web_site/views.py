from django.shortcuts import render
from django.http import HttpResponse, Http404
from web_site.models import Event, Project, Photos, Contact
from web_site.admin import ContactAdmin, load_json_file
from vlastik_site import settings
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
    try:
        contact_list = load_json_file(settings.CONTACT_JSON_FILE)
        context = {"contact_list":  contact_list}
    except:
        # raise Http404("Contacts are emtpy")
        context = {}
    
    return render(request, "web_site/contact.html", context)

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

def about_me(request):
    content = load_json_file(settings.ABOUT_ME_JSON_FILE)
    return render(request, "web_site/about_me.html", content)

