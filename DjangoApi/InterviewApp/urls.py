from django.urls import re_path
from InterviewApp import views

urlpatterns = [
    re_path(r"^interviewer/$", views.interviewer),
    re_path(r"^interviewer/([0-9]+)$", views.interviewer),
    re_path(r"^interviewee/$", views.interviewer),
    re_path(r"^interviewee/([0-9]+)$", views.interviewer),
    re_path(r"^interviewer-slot/$", views.interviewer_slot),
    re_path(r"^interviewer-slot/(?P<interviewer_id>[a-z0-9]+)$", views.interviewer_slot),
    re_path(
        r"^interviewer-slot/(?P<interviewer_id>[a-z0-9]+)/(?P<year>[0-9]{4})/$",
        views.interviewer_slot,
    ),
    re_path(
        r"^interviewer-slot/(?P<interviewer_id>[a-z0-9]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$",
        views.interviewer_slot,
    ),
    re_path(
        r"^interviewer-slot/(?P<interviewer_id>[a-z0-9]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$",
        views.interviewer_slot,
    ),
    re_path(r"^interviewee-slot/$", views.interviewee_slot),
    re_path(r"^interviewee-slot/(?P<interviewee_id>[a-z0-9]+)$", views.interviewee_slot),
    re_path(
        r"^interviewee-slot/(?P<interviewee_id>[a-z0-9]+)/(?P<year>[0-9]{4})/$",
        views.interviewee_slot,
    ),
    re_path(
        r"^interviewee-slot/(?P<interviewee_id>[a-z0-9]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$",
        views.interviewee_slot,
    ),
    re_path(
        r"^interviewee-slot/(?P<interviewee_id>[a-z0-9]+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$",
        views.interviewee_slot,
    ),
    re_path(r"^find-available-slots/$", views.find_available_slots),
]
