from django.db import models
from django.utils import timezone


class Interviewer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True)


class Interviewee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)


class InterviewerAvaliableTimeSlots(models.Model):
    interviewer = models.ForeignKey(
        "Interviewer",
        on_delete=models.CASCADE,
    )
    available_date = models.DateField(default=timezone.now)
    ipayload1 = models.BigIntegerField(default=0)
    ipayload2 = models.BigIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["interviewer", "available_date"], name="unique_interviewer_slot"
            )
        ]


class IntervieweeAvaliableTimeSlots(models.Model):
    interviewee = models.ForeignKey(
        "Interviewee",
        on_delete=models.CASCADE,
    )
    available_date = models.DateField(default=timezone.now)
    ipayload1 = models.BigIntegerField(default=0)
    ipayload2 = models.BigIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["interviewee", "available_date"], name="unique_interviewee_slot"
            )
        ]
