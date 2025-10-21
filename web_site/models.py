from django.db import models

# from datetime import datetime, tzinfo, timezone, timedelta
import pytz
import locale
import json
from django.dispatch import receiver
from vlastik_site import settings
import os
import uuid

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


class Photos(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulek")
    photo = models.ImageField(verbose_name="foto")

    class Meta:
        verbose_name = "Fotka"
        verbose_name_plural = "Fotky"

    def __str__(self):
        return self.title + ": " + self.photo.path


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