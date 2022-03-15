from rest_framework import serializers
from InterviewApp.models import (Interviewee,
                IntervieweeAvaliableTimeSlots, 
                Interviewer, 
                InterviewerAvaliableTimeSlots)

class InterviewerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Interviewer
        fields = ("id","name","email")
        
    def validate_email(self, value):
        if Interviewer.objects.filter(email__iexact= value).exists():
            raise serializers.ValidationError("Email already exists please choose another")
        return value

class IntervieweeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Interviewee
        fields = ("id","name","email")
        
    def validate_email(self, value):
        if Interviewer.objects.filter(email__iexact= value).exists():
            raise serializers.ValidationError("Email already exists please choose another")
        return value

class InterviewerSlotQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewerAvaliableTimeSlots
        fields = ("id","interviewer","start_time","end_time")
        depth = 1

class InterviewerSlotMutateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewerAvaliableTimeSlots
        fields = ("id","interviewer","start_time","end_time")

class IntervieweeSlotQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervieweeAvaliableTimeSlots
        fields = ("id","interviewee","start_time","end_time")
        depth = 1

class IntervieweeSlotMutateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervieweeAvaliableTimeSlots
        fields = ("id","interviewee","start_time","end_time")