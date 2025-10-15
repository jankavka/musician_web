from django.contrib import admin

# Register your models here.

from .models import Event, Project, Photos,Contact

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Photos)
admin.site.register(Contact)


