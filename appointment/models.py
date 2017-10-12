# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from accounts.models import user,patient,doctor
# Create your models here.
class location(models.Model):
    address = models.CharField(max_length=50) #this address means local address+city
    # time_schedule will be changed to some other type in future
    day = models.CharField(max_length=20,default="Fri") #staring time at this location


    def _str_(self):
        return self.address

# many to many relation
class Doctor_has_sitting_on_location(models.Model):
    doctor = models.ForeignKey(doctor)
    location = models.ForeignKey(location)
    end_date = models.CharField(max_length=50,default="N/A") #normally doctor hasn't ended his sitting on this location
    fee = models.IntegerField

    def __str__(self):
        return doctor.name



class appointment(models.Model):
    # 4 statuses. Pending , Approved, Rejected, Closed
    status = models.CharField(max_length=50,default="Pending Approval")
    #approval = models.CharField(max_length=2)
    #requested_date = models.CharField(max_length=20,default="Fri")   # search google to see how to work with this

    patient = models.ForeignKey(patient,on_delete = models.CASCADE)
    sitting = models.ForeignKey(Doctor_has_sitting_on_location, on_delete = models.CASCADE)
    user = models.ForeignKey(user, on_delete = models.CASCADE)

    def _str_(self):
        return self.status

