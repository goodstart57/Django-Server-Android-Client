from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^member$', views.getMemInfo),
    url(r'^member', views.getMemInfo),
    url(r'^recommend$', views.getRecoList),
    url(r'^register$', views.postMemberExample),
    url(r'^insertSignup$', views.postMember),
    url(r'^insertSignupAll$', views.postMemberAll),
    url(r'^insertMatchAll$', views.postMatchAll),
    url(r'^ListAllUserIDs$', views.listAllUserIDs),
]
