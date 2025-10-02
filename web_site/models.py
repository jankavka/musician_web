from django.db import models

# Create your models here.


class Event(models.Model):
    event_title = models.CharField(max_length=200, verbose_name="Název události")
    band = models.CharField(max_length=200, verbose_name="kapela")
    start_of_event = models.DateTimeField("datum akce")

    class Meta:
        verbose_name = "Událost"
        verbose_name_plural = "Události"

    def __str__(self):
        return self.event_title + ", " +  self.band + ", " + self.start_of_event


class Project(models.Model):
    band_name = models.CharField(max_length=200, verbose_name="název projektu")
    description = models.TextField(verbose_name="popis")

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"


    def __str__(self):
        return self.band_name + ", " + self.description