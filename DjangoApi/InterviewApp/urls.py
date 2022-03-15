from django.urls import re_path
from InterviewApp import views
urlpatterns = [
    re_path(r'^interviewer/$',views.interviewer),
    re_path(r'^interviewer/([0-9]+)$',views.interviewer),
    re_path(r'^interviewee/$',views.interviewer),
    re_path(r'^interviewee/([0-9]+)$',views.interviewer),
    re_path(r'^interviewer-slot/$',views.interviewer_slot),
    re_path(r'^interviewer-slot/([0-9]+)$',views.interviewer_slot),
    re_path(r'^interviewee-slot/$',views.interviewee_slot),
    re_path(r'^interviewee-slot/([0-9]+)$',views.interviewee_slot),
    re_path(r'^find-available-slots/$',views.find_available_slots),
]