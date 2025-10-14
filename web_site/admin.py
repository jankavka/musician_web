from django.contrib import admin

# Register your models here.

from .models import Event, Project, Photos

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Photos)
