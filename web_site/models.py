from django.db import models

import pytz
import locale
import re
import random

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název události")
    band = models.CharField(max_length=200, verbose_name="kapela")
    start_of_event = models.DateTimeField("datum akce")
    link = models.CharField(max_length=200, verbose_name="odkaz")

    class Meta:
        verbose_name = "Koncert"
        verbose_name_plural = "Koncerty"
        locale.setlocale(locale.LC_ALL, "cs_CZ")

    def __str__(self):
        event_local_time = self.start_of_event.astimezone(
            pytz.timezone("Europe/Prague")
        )
        formatted_local_time = event_local_time.strftime("%d. %B %Y, %H:%M")
        return self.title + ", " + self.band + ", " + str(formatted_local_time)


class Project(models.Model):
    band_name = models.CharField(max_length=200, verbose_name="název projektu")
    description = models.TextField(verbose_name="popis")

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"

    def __str__(self):
        return self.band_name + ", " + self.description


class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulek")
    photo = models.ImageField(verbose_name="foto")

    class Meta:
        verbose_name = "Fotka"
        verbose_name_plural = "Fotky"

    def __str__(self):
        return self.title + ": " + self.photo.path


class Video(models.Model):
    link = models.CharField(max_length=200, verbose_name="odkaz")
    title = models.CharField(max_length=200, verbose_name="popisek")
    normalized_title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videa"

    def extract_videoId(self):
        if self.link.startswith("http"):
            index = self.link.find("v=") + 2
            video_id = self.link[index:]
            self.link = video_id
        if "&" in self.link:
            end_of_video_id = self.link.find("&")
            self.link = self.link[:end_of_video_id]

    def normalize_title(self):
        string_to_normalize = self.title
        if( re.search("\s", string_to_normalize)):
            string_to_normalize = re.sub("\s", "-", string_to_normalize)
        if( re.search("[ěščřžýáíéťď]", string_to_normalize)):
            string_to_normalize = re.sub("[ěščřžýáíéťď]", "-", string_to_normalize)
        number = random.randint(0,1000)
        string_to_normalize = string_to_normalize + str(number)
        self.normalized_title = string_to_normalize.lower().strip()

            

    def save(self, *args, **kwargs):
        self.extract_videoId()
        self.normalize_title()
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return "Jméno: " + self.title + ", norm title: " + self.normalized_title


class Contact(models.Model):

    class Meta:
        managed: False
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakty"


class AboutMe(models.Model):

    class Meta:
        managed: False
        verbose_name = "O mě"
        verbose_name_plural = "O mě"
