# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    email= models.CharField(max_length=30,default="N/A")
    logged_in = models.IntegerField(default=0)

    def __str__(self):
        return self.username




class doctor(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=50,default="abc")
    email = models.CharField(max_length=30, default="N/A")
    contact_no = models.CharField(max_length=20,default="012")
    BMDC_reg_no = models.CharField(max_length=50)
    degree = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100)
    app_time_per_patient = models.CharField(max_length=20,default= "20") #how much time each patient will get
    logged_in = models.IntegerField(default=0)

    def __str__(self):
        return self.BMDC_reg_no + '-' + self.name

#patient will be created inside profile of user.So it may be needed to cut paste to profile app
class patient(models.Model):
    user = models.ForeignKey(user,on_delete = models.CASCADE) #coz user gone,patient gone
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=20)
    guardian = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    age = models.CharField(max_length=20,default="50")


    def __str__(self):
        return self.user + '-' + self.name





