from django.conf.urls import url

from . import views

app_name = "appointment"

urlpatterns = [
    #call from home page user
    url(r'^request_appointment/(?P<user_id>[0-9]+)/$', views.show_get_app1,name="get_app1"),

    #call after patient data fill up
    url(r'^request_appointment2/(?P<user_id>[0-9]+)/$', views.show_get_app2,name="get_app2"),


    url(r'^request_appointment3/(?P<user_id>[0-9]+)/(?P<patient_id>[0-9]+)/$', views.show_get_app3,name="get_app3"),

    #appointment done.
    url(r'^request_appointment4/(?P<user_id>[0-9]+)/(?P<patient_id>[0-9]+)/(?P<doctor_id>[0-9]+)$', views.show_get_app4, name="get_app4"),

    url(r'^location_add/(?P<doctor_id>[0-9]+)$', views.add_location,name="add_location"),


    url(r'^appointment_done/(?P<user_id>[0-9]+)/(?P<patient_id>[0-9]+)/(?P<doctor_id>[0-9]+)$', views.appointment_done,name="app_done"),



    url(r'^check_pending/(?P<doctor_id>[0-9]+)$',views.check_pending,name="check_pending"),


    url(r'^location_page_load/(?P<doctor_id>[0-9]+)$',views.location_page_load,name="location_page_load"),


    #url(r'^doctor_home/',views.doctor_registration,name="checkCompletedDocReg"),


]
