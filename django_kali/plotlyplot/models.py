from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class fao_forest_data(models.Model):
    ELEM = models.CharField(max_length=100)
    AREA_NEW = models.CharField(max_length=100)
    GOAL = models.CharField(max_length=100)
    value_footnotes = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    VALUE = models.IntegerField()
    YEAR = models.IntegerField()
    element_code = models.IntegerField()
    def __str__(self):
        return (self.YEAR,self.VALUE,self.AREA_NEW)

class scrapingtweets(models.Model):
    #id = models.IntegerField()
    user = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    date = models.DateField()
    def __str__(self):
        return (self.date,self.user,self.text)

"""class data_geo(models.Model):

class geojson(models.Model):
    id = models.IntegerField()
    json = models.CharField(max=100000000)
    def __str__(self):
        return (self.json)"""
