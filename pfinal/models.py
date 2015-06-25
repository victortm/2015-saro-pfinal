from django.db import models
import datetime

# Create your models here.

class activitie(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    pickdate = models.DateField(blank=True, null=True)
    cost = models.CharField(max_length=20,blank=True, null=True)
    kind = models.CharField(max_length=200, blank=True, null=True)
    longlength = models.BooleanField(default=False)
    moreinfo = models.CharField(max_length=400, blank=True, null=True)

class myacc(models.Model):
    name = models.CharField(max_length= 32, primary_key = True)
    activity = models.ManyToManyField(activitie)
