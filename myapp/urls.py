from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path("", views.index, name="LNHome"),
   path("about", views.about, name="about"),
   path("contact", views.contact, name="contact"),
   path("contactus", views.contactus, name="contactus"),
   path("signup", views.signup, name="signup"),
   path("login", views.login, name="login"),
   path('viewdata', views.viewdata, name='viewdata'),
   path('checkuser', views.checklogin, name='checkuser'),
   path("logout", views.logout, name="Logout"),
   path("completeprofileuser", views.completeprofileuser, name="completeprofileuser"),
   path("completeprofilecomp", views.completeprofilecomp, name="completeprofilecomp"),
   path("completeprofilecompsubmit", views.completeprofilecompsubmit, name="completeprofilecompsubmit"),
   path("completeprofile", views.completeprofile, name="completeprofile"),
   path("companyprofilepage", views.companyprofilepage, name="companyprofilepage"),
   path("profilepage", views.profilepage, name="profilepage"),
   path("deleteresume", views.deleteresume, name="deleteresume"),
   path("resumeupload", views.resumeupload, name="resumeupload"),
   path("editprofile", views.editprofile, name="editprofile"),
   path("editprofilecompany", views.editprofilecompany, name="editprofilecompany"),
   path("editprofilecompsubmit", views.editprofilecompsubmit, name="editprofilecompsubmit"),
   path("editprofilesubmit", views.editprofilesubmit, name="editprofilesubmit"),
   path("changedp", views.changedp, name="changedp"),
   path("changepw", views.changepw, name="changepw"),
   path("addjob", views.addjob, name="addjob"),
   path("postjob", views.postjob, name="postjob"),
   path("youropenings", views.youropenings, name="youropenings"),
   path("alljobs", views.alljobs, name="alljobs"),
   path("viewyourapplications", views.viewyourapplications, name="viewyourapplications"),
   path("viewcandidates", views.viewcandidates, name="viewcandidates"),
   path("deletejob/<int:jid>", views.deletejob, name="deletejob"),
   path("applyjob/<int:ajid>", views.applyjob, name="applyjob"),
   path("deleteapplication/<int:daid>", views.deleteapplication, name="deleteapplication"),
   path("showinterest/<int:siid>", views.showinterest, name="showinterest"),
   path("rejectcandidate/<int:rcid>", views.rejectcandidate, name="rejectcandidate"),
]