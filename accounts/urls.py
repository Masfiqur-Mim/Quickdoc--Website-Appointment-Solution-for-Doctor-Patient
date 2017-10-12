from django.conf.urls import url

from . import views

app_name = "accounts"

urlpatterns = [

    url(r'^sign_in/', views.sign_in_page_show,name="sign_in_page"),

    url(r'^profile_user/(?P<user_id>[0-9]+)$', views.user_profile, name="user_profile"),

    url(r'^profile_doc/(?P<doc_id>[0-9]+)$', views.doc_profile, name="doc_profile"),



    url(r'^registration/user/', views.user_reg_page_show,name="user_reg"),
    url(r'^registration/doctor/', views.doc_reg_page_show,name="doc_reg"),

    #url(r'^diagnostics/', views.diagnostics_registration),

    url(r'^user_home/',views.user_registration,name="checkCompletedUserReg"),
    url(r'^doctor_home/',views.doctor_registration,name="checkCompletedDocReg"),

    url(r'^user_sign_in_check', views.user_sign_in, name="user_sign_in"),

    url(r'^doc_sign_in_check', views.doc_sign_in, name="doc_sign_in"),

]
