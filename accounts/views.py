# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import user,doctor
from django.http import request
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def user_reg_page_show(request):
    template=loader.get_template('accounts/registration_user.html')
    context=[]
    return HttpResponse(template.render({},request))


def doc_reg_page_show(request):
    template=loader.get_template('accounts/registration_doctor.html')
    context=[]
    return HttpResponse(template.render({},request))


def sign_in_page_show(request):

    return render(request,"accounts/sign_in.html",{})




def user_sign_in(request):

    userObj = user.objects.filter(username=request.POST.get("username","") ,password=request.POST.get("pass",""))[0]

    if userObj:
        userObj.logged_in=1
        userObj.save()
        return render(request,"accounts/home_user.html",{'user_counter': userObj.pk})

    else:
        return render(request,"accounts/sign_in.html",{})


def doc_sign_in(request):
    all_docObj = doctor.objects.filter(BMDC_reg_no=request.POST.get("doc_bmdc", ""), password=request.POST.get("doc_pass", ""))

    if all_docObj:
        docObj=all_docObj[0]

        docObj.logged_in=1

        docObj.save()

        return render(request, "accounts/home_doctor.html", {'doc_counter': docObj.pk})

    else:
        return render(request, "accounts/sign_in.html", {})


def user_registration(request):
    userObj = user()
    print "running"
    if request.POST:
        if request.POST.get("pass","") == request.POST.get("conf_pass",""):
            userObj.firstname=request.POST.get("first_name","")
            userObj.lastname=request.POST.get("last_name","")
            userObj.username=request.POST.get("username","")
            userObj.email=request.POST.get("email","")
            userObj.password=request.POST.get("pass","")
            userObj.contact_no = request.POST.get("mobile", "")

            userObj.logged_in=1

            userObj.save()

            template = loader.get_template("accounts/home_user.html")
            #return HttpResponse(template.render({},request))
            return render(request,"accounts/home_user.html",{'user_counter': userObj.pk})
        else:
            # password wrong msg
            template = loader.get_template("accounts/registration_user.html")

            return HttpResponse(template.render({},request))
    else:
            # password wrong msg
            template = loader.get_template("accounts/registration_user.html")

            return HttpResponse(template.render({},request))



def doctor_registration(request):
    doctorObj = doctor()
    if request.POST:
        if request.POST.get("doc_pass","") == request.POST.get("doc_conf_pass",""):
            doctorObj.name=request.POST.get("doc_name","")
            doctorObj.gender = request.POST.get("doc_gender","")
            doctorObj.password = request.POST.get("doc_pass","")
            doctorObj.email = request.POST.get("doc_email","")
            doctorObj.contact_no = request.POST.get("doc_mobile","")
            doctorObj.BMDC_reg_no = request.POST.get("doc_bmdc","")
            doctorObj.degree = request.POST.get("doc_degree","")
            doctorObj.specialty=request.POST.get("doc_specialty","")
            doctorObj.app_time_per_patient=request.POST.get("patient_app_time","")

            doctorObj.logged_in=1

            doctorObj.save()

            #return HttpResponse("<h1>done</h1>")
            print (doctorObj.pk)
            return render(request, "accounts/home_doctor.html", {'doc_counter': doctorObj.pk})

        else:
        # show password wrong msg and the registration page
            template = loader.get_template("accounts/registration_doctor.html")

            return HttpResponse(template.render({}, request))
    else:
        # show password wrong msg and the registration page
        template = loader.get_template("accounts/registration_doctor.html")

        return HttpResponse(template.render({}, request))


def user_profile(request,user_id):

    userObj= user.objects.filter(pk=user_id)[0]
    return render(request,"accounts/profile_user.html",{'user':userObj})


def doc_profile(request,doc_id):
    docObj = doctor.objects.filter(pk=doc_id)[0]
    return render(request,"accounts/profile_doctor.html",{'doctor':docObj})





def diagnostics_registration(request):
    print "abc"