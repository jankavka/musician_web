from django.contrib import admin, messages
from vlastik_site import settings
from django.shortcuts import render, redirect
from django import forms
from django.urls import path
import json

# Register your models here.

from .models import Event, Project, Photo, Contact, AboutMe, Video


admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Photo)



class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    telephone = forms.CharField(label="Telefón")


def load_json_file(path):
    data = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(obj=None, fp=f)
        # raise FileNotFoundError("File with content not found")


def save_contact(email, telephone):
    path = settings.CONTACT_JSON_FILE
    data = {"email": email, "telephone": telephone}
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)
    except:
        raise RuntimeError("Saving content not successfull")


def save_aboutme(data):
    path = settings.ABOUT_ME_JSON_FILE
    content = {"content" : data}
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(content, f)
    except:
        raise RuntimeError("Saving content not successfull")


class ContactAdmin(admin.ModelAdmin):
    change_list_template = "web_site/admin/contact_admin.html"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):

        urls = super().get_urls()
        my_urls = [
            path("", self.admin_site.admin_view(self.edit_view), name="contact_admin")
        ]

        return my_urls + urls

    def edit_view(self, request):
        initial_values = load_json_file(settings.CONTACT_JSON_FILE)

        if request.method == "POST":
            form = ContactForm(request.POST)

            if form.is_valid():
                save_contact(form.cleaned_data["email"], form.cleaned_data["telephone"])
                messages.success(request=request, message="Kontakt úspěšně uložen")
                return redirect("/admin")
            else:
                messages.error(request=request, message="Nepodařilo se uložit contact")
                return redirect("admin:contact_admin")

        else:
            data = ContactForm(initial=initial_values)

            return render(
                request,
                "web_site/admin/contact_admin.html",
                {"title": "Editace kontaktu", "data": data},
            )


admin.site.register(Contact, ContactAdmin)


class AboutMeForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    #content = forms.CharField(widget=TinyMCE())
    #content = tinymce_models.HTMLField()



class AboutMeAdmin(admin.ModelAdmin):
    change_list_template = "web_site/admin/contact_admin.html"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):

        urls = super().get_urls()

        my_urls = [
            path("", self.admin_site.admin_view(self.my_view), name="aboutme_admin")
        ]

        return my_urls + urls

    def my_view(self, request):
        initial_values = load_json_file(settings.ABOUT_ME_JSON_FILE)
        if request.method == "POST":
            form = AboutMeForm(request.POST)
            if form.is_valid():
                save_aboutme(form.cleaned_data["content"])
                messages.success(request, "Obsah úspěšně uložen")
                return redirect("/admin")
            else:
                messages.error(request, "form data not valid")
                return redirect("admin:aboutme_admin")

        else:
            content = AboutMeForm(initial_values)
            return render(
                request,
                "web_site/admin/aboutme_admin.html",
                {"title": "O mě", "content": content},
            )


admin.site.register(AboutMe, AboutMeAdmin)


class VideoAdmin(admin.ModelAdmin):
    exclude = ["normalized_title", "youtube_video_id"]


admin.site.register(Video, VideoAdmin)
