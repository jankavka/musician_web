from django.db import models

# Create your models here.


class Events(models.Model):
    event_title = models.CharField(max_length=200, verbose_name="Název události")
    band = models.CharField(max_length=200, verbose_name="kapela")
    start_of_event = models.DateTimeField("datum akce")


class Projects(models.Model):
    band_name = models.CharField(max_length=200, verbose_name="název projektu")
    description = models.TextField(verbose_name="popis")