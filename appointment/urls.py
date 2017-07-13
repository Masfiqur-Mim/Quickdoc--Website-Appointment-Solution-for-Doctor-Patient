from django.conf.urls import url

from . import views

app_name = "accounts"

urlpatterns = [
    url(r'^registration/user/', views.user_reg_page_show),
    url(r'^registration/doctor/', views.doc_reg_page_show),
    #url(r'^diagnostics/', views.diagnostics_registration),
    url(r'^user_home/',views.user_registration,name="checkCompletedUserReg"),
    url(r'^doctor_home/',views.doctor_registration,name="checkCompletedDocReg"),


]
