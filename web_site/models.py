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
    photo = models.ImageField(verbose_name="foto")

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"

    def __str__(self):
        return self.band_name


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
    youtube_video_id = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videa"

    # extracts videoID for later use in player_api script in template
    def extract_video_id(self):
        if self.youtube_video_id.strip() == "":
            index = self.link.find("v=") + 2
            video_id = self.link[index:]
            self.youtube_video_id = video_id
            if "&" in self.youtube_video_id:
                end_of_video_id = self.youtube_video_id.find("&")
                self.youtube_video_id = self.youtube_video_id[:end_of_video_id]

    # normalizes title for later use as a CSS selector in template
    def normalize_title(self):
        if self.normalized_title.strip() == "":
            string_to_normalize = self.title.strip()
            string_to_normalize = re.sub("\s", "-", string_to_normalize)
            string_to_normalize = re.sub("[ěščřžýáíéťď]", "-", string_to_normalize)
            number = random.randint(0, 1000)
            string_to_normalize = string_to_normalize + str(number)
            self.normalized_title = string_to_normalize.lower().strip()

    def save(self, *args, **kwargs):
        self.extract_video_id()
        self.normalize_title()
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return "Titulek: " + self.title 


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
        
