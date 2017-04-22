# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Users(models.Model):
#     name = models.CharField(max_length=200);
class Users(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    def __unicode__(self):
        return self.first_name

class Data(models.Model):
    eating = models.BigIntegerField(null=True)
     #1-5
    drinking = models.BigIntegerField(null=True)
    #0-8

    toileting = models.BigIntegerField(null=True)
    #1-10
    
    showering = models.BigIntegerField(null=True)
    #1-3
    
    leaving = models.BigIntegerField(null=True)
    #1-12
    sleeping = models.BigIntegerField(null=True)
    #4-10
    
    weight = models.FloatField(default=0.0)
    #40-130
    
    
       
    