# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

from accounts.models import user
from accounts.models import patient,doctor
from .models import location,Doctor_has_sitting_on_location,appointment

# Create your views here.


def show_get_app1(request,user_id):
            #return HttpResponse(template.render({},request))
        userObj= user.objects.filter(pk=user_id)[0]
        return render(request,"appointment/get_appointment1.html",{'user': userObj,'range': range(120)})



#save patient data and show get appointment page 2
def show_get_app2(request,user_id):
    patientObj = patient()

    userObj = user.objects.filter(pk=user_id)[0]
    print "running in app"
    if request.POST:

            patientObj.user=userObj
            patientObj.name = request.POST.get("pName", "")
            patientObj.gender = request.POST.get("pGender", "")
            patientObj.contact_no = request.POST.get("pContact", "")
            patientObj.guardian = request.POST.get("pGuardian", "")
            patientObj.city = request.POST.get("pCity", "")
            patientObj.area = request.POST.get("pArea", "")
            patientObj.age = request.POST.get("pAge","")
            patientObj.save()


            # return HttpResponse(template.render({},request))
            return render(request, "appointment/get_appointment2.html",
                          {'user_counter': userObj.pk,'patient_counter':patientObj.pk})
    else:
        return render(request, "appointment/get_appointment1.html", {'user': userObj, 'range': range(120)})


def show_get_app3(request,user_id,patient_id):
    if request.POST:
        all_doc= doctor.objects.filter(specialty=request.POST.get("doc_category",""))

        return render(request, "appointment/get_appointment3.html",
                      {'user_counter': user_id, 'patient_counter': patient_id,'search_result':all_doc})




    else:
        return render(request, "appointment/get_appointment2.html",
                      {'user_counter': user_id, 'patient_counter': patient_id})


def show_get_app4(request,user_id,patient_id,doctor_id):

        docObj=doctor.objects.filter(pk=doctor_id)[0]
        all_sittings = docObj.doctor_has_sitting_on_location_set.all()


        return render(request,"appointment/get_appointment4.html",
                      {'sittings':all_sittings,'user_counter': user_id,'patient_counter':patient_id,
                       'doctor_counter':doctor_id})


def appointment_done(request,user_id,patient_id,doctor_id):

    new_app= appointment()

    if request.POST:
        new_app.patient = patient.objects.filter(pk=patient_id)[0]

        new_app.user = user.objects.filter(pk=user_id)[0]

        sitting_pk= request.POST.get("doc_has_sitting_pk","")

        new_app.sitting = Doctor_has_sitting_on_location.objects.filter(pk=sitting_pk)[0]

        new_app.save()

        docObj = doctor.objects.filter(pk=doctor_id)[0]

        return render(request,"appointment/get_appointment_done.html",{'doctor':doctor})


    else:
        docObj = doctor.objects.filter(pk=doctor_id)[0]
        all_sittings = docObj.doctor_has_sitting_on_location_set.all()

        return render(request,"appointment/get_appointment4.html",
                      {'sittings':all_sittings,'user_counter': user_id,'patient_counter':patient_id,
                       'doctor_counter':doctor_id})





def check_pending(request,doctor_id):

    docObj = doctor.objects.filter(pk=doctor_id)[0]
    sitting = docObj.doctor_has_sitting_on_location_set.all()
    apps = []
    for sit in sitting:
        tmp = sit.appointment_set.filter(status = "Pending Approval")
        for d in tmp.all():
            apps = apps + [d]

    pending_apps = apps

    return render(request, "appointment/pending_apps.html", {'pending_apps': pending_apps})




def location_page_load(request,doctor_id):
    return render(request,"appointment/Add_location.html",{'doctor_id':doctor_id})






def add_location(request,doctor_id):
    locObj= location()
    doc_has_sitting = Doctor_has_sitting_on_location()
    if request.POST:
        locObj.address= request.POST.get("location_area","") +","+ request.POST.get("location_city","")
        locObj.day = request.POST.get("location_day","")

        locObj.save()

        #location obj done

        docObj= doctor.objects.filter(pk=doctor_id)[0]

        doc_has_sitting.doctor=docObj

        doc_has_sitting.location = locObj

        doc_has_sitting.fee = request.POST.get("fee","")

        doc_has_sitting.save()



    return render(request, "accounts/home_doctor.html", {'doc_counter': doctor_id})




