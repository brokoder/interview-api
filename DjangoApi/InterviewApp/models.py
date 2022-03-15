from django.db import models 

class Interviewer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100,unique=True)

class Interviewee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    
class InterviewerAvaliableTimeSlots(models.Model):
    interviewer = models.ForeignKey(
        'Interviewer',
        on_delete=models.CASCADE,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class IntervieweeAvaliableTimeSlots(models.Model):
    interviewee = models.ForeignKey(
        'Interviewee',
        on_delete=models.CASCADE,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()