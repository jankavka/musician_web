from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("koncerty", views.concerts, name="concerts"),
    path("kontakt", views.contact, name="contant"),
    path("projekty", views.projects, name="projects"),
    path("fotky", views.photos, name="photos"),
    path("videa", views.videos, name="videos")
]