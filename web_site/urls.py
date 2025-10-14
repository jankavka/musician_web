from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path
from django.views.static import serve

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("koncerty", views.concerts, name="concerts"),
    path("kontakt", views.contact, name="contant"),
    path("projekty", views.projects, name="projects"),
    path("fotky", views.photos, name="photos"),
    path("videa", views.videos, name="videos")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(
#             r"^uploads/(?P<path>.*)$",
#             serve,
#             {
#                 "document_root": settings.MEDIA_ROOT,
#             },
#         ),
#     ]