# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from accounts.models import user,patient,doctor
from appointment.models import location,Doctor_has_sitting_on_location,appointment

# Create your models here.
class review(models.Model):
    time = models.DateTimeField(default= datetime.now)
    rating = models.IntegerField
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE) #don't cascade.confusing fact
    appointment = models.ForeignKey(appointment,on_delete=models.CASCADE)
    #the user data is in appointment table.So no worries

    def __str__(self):
        return user.username + '-' + doctor.name

class comment(models.Model):
    #we don't need to distinctly specify the commenter name here,
    # bcoz the review poster is the commenter here
    text = models.CharField(max_length=1000)
    time = models.DateTimeField(default=datetime.now)
    review = models.ForeignKey(review,on_delete = models.CASCADE)



class reply_on_comment(models.Model):
    #we need to know who posted this reply here. So we need to store the username of that user here
    text = models.CharField(max_length=1000)
    time = models.DateTimeField(default=datetime.now)
    parent_comment = models.ForeignKey(comment,on_delete = models.CASCADE)
    user = models.ForeignKey(user)#getting the user who posted the reply

    def _str_(self):
        return user.username + '-' + self.text

