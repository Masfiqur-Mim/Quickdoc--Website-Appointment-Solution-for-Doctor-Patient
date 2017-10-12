# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import user,patient,doctor

# Register your models here.
class admin_sees_users(admin.ModelAdmin):
    fieldsets = [
        ('First Name' , {'fields' : ['firstname']}),
        ('Last Name', {'fields': ['lastname']}),
        ('User Name', {'fields': ['username']}),
        ('Contact No.', {'fields': ['contact_no']}),
    ]

    list_display =  [('username')]
    #list_filter = []
    search_fields = ['firstname','lastname']




class admin_sees_doctors(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Gender', {'fields': ['gender']}),
        ('Contact No.', {'fields': ['contact_no']}),
        ('Degree', {'fields': ['degree']}),
        ('BMDC Reg No', {'fields': ['BMDC_reg_no']}),
        ('Specialty', {'fields': ['specialty']}),
    ]

    list_display = ('name','BMDC_reg_no','specialty')
    list_filter = ['degree','specialty']
    search_fields = ['firstname', 'lastname']




class admin_sees_patients(admin.ModelAdmin):
    fieldsets = [
        ('Username', {'fields': ['user.username']}),
        ('Name', {'fields': ['name']}),
        ('Gender', {'fields': ['gender']}),
        ('Contact No.', {'fields': ['contact_no']}),
        ('Guardian', {'fields': ['Guardian']}),
        ('City', {'fields': ['city']}),
        ('Area', {'fields': ['area']}),
    ]
    thisUser=patient.user
    username=thisUser.__str__()
    list_display = ('name','username')
    list_filter = ['city','gender']
    search_fields = ['city', 'name']


admin.site.register(user, admin_sees_users)
admin.site.register(doctor, admin_sees_doctors)
admin.site.register(patient, admin_sees_patients)