from django.db import models
from datetime import datetime, tzinfo, timezone, timedelta
import pytz
import locale

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název události")
    band = models.CharField(max_length=200, verbose_name="kapela")
    start_of_event = models.DateTimeField("datum akce")

    class Meta:
        verbose_name = "Událost"
        verbose_name_plural = "Události"
        locale.setlocale(locale.LC_ALL, "cs_CZ")

    def __str__(self):
        event_local_time = self.start_of_event.astimezone(pytz.timezone("Europe/Prague"))
        formatted_local_time = event_local_time.strftime("%d. %B %Y, %H:%M")
        return (
            self.title
            + ", "
            + self.band
            + ", "
            + str(formatted_local_time)
            
        )


class Project(models.Model):
    band_name = models.CharField(max_length=200, verbose_name="název projektu")
    description = models.TextField(verbose_name="popis")

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"

    def __str__(self):
        return self.band_name + ", " + self.description
