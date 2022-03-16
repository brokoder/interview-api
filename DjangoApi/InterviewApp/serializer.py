from rest_framework import serializers
from InterviewApp.models import (
    Interviewee,
    IntervieweeAvaliableTimeSlots,
    Interviewer,
    InterviewerAvaliableTimeSlots,
)
from InterviewApp.adaptors import (
    convert_time_list_to_big_ints,
    convert_big_ints_to_time_list,
)
from django.db.utils import IntegrityError


class InterviewerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Interviewer
        fields = ("id", "name", "email")

    def validate_email(self, value):
        if Interviewer.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "Email already exists please choose another"
            )
        return value


class IntervieweeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Interviewee
        fields = ("id", "name", "email")

    def validate_email(self, value):
        if Interviewee.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "Email already exists please choose another"
            )
        return value


class InterviewerSlotQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewerAvaliableTimeSlots
        fields = ("id", "interviewer", "available_date", "ipayload1", "ipayload2")
        depth = 1


class InterviewerSlotMutateSerializer(serializers.ModelSerializer):
    avaliable_slots = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=23)
    )

    class Meta:
        model = InterviewerAvaliableTimeSlots
        fields = ("id", "interviewer", "available_date", "avaliable_slots")

    def validate(self, data):
        if "interviewer" not in data.keys():
            raise serializers.ValidationError("'interviewer' key missing")
        elif "available_date" not in data.keys():
            raise serializers.ValidationError("'available_date' key missing")
        elif "avaliable_slots" not in data.keys():
            raise serializers.ValidationError("'avaliable_slots' key missing")
        return data

    def create(self, validated_data):
        validated_data["interviewer_id"] = validated_data["interviewer"]
        (
            validated_data["ipayload1"],
            validated_data["ipayload2"],
        ) = convert_time_list_to_big_ints(validated_data["avaliable_slots"])
        del validated_data["avaliable_slots"], validated_data["interviewer"]
        InterviewerAvaliableTimeSlots.objects.create(**validated_data)
        return None

    def update(self, validated_data):
        validated_data["interviewer_id"] = validated_data["interviewer"]
        (
            validated_data["ipayload1"],
            validated_data["ipayload2"],
        ) = convert_time_list_to_big_ints(validated_data["avaliable_slots"])
        del validated_data["avaliable_slots"], validated_data["interviewer"]
        print(validated_data)
        InterviewerAvaliableTimeSlots.objects.filter(
            interviewer_id=validated_data["interviewer_id"],
            available_date=validated_data["available_date"],
        ).update(**validated_data)
        return None


class IntervieweeSlotQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervieweeAvaliableTimeSlots
        fields = ("id", "interviewee", "available_date", "ipayload1", "ipayload2")
        depth = 1


class IntervieweeSlotMutateSerializer(serializers.ModelSerializer):
    avaliable_slots = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=23)
    )

    class Meta:
        model = IntervieweeAvaliableTimeSlots
        fields = ("id", "interviewee", "available_date", "avaliable_slots")

    def validate(self, data):
        if "interviewee" not in data.keys():
            raise serializers.ValidationError("'interviewee' key missing")
        elif "available_date" not in data.keys():
            raise serializers.ValidationError("'available_date' key missing")
        elif "avaliable_slots" not in data.keys():
            raise serializers.ValidationError("'avaliable_slots' key missing")
        return data

    def create(self, validated_data):
        validated_data["interviewee_id"] = validated_data["interviewee"]
        (
            validated_data["ipayload1"],
            validated_data["ipayload2"],
        ) = convert_time_list_to_big_ints(validated_data["avaliable_slots"])
        del validated_data["avaliable_slots"], validated_data["interviewee"]
        IntervieweeAvaliableTimeSlots.objects.create(**validated_data)
        return None

    def update(self, validated_data):
        validated_data["interviewee_id"] = validated_data["interviewee"]
        (
            validated_data["ipayload1"],
            validated_data["ipayload2"],
        ) = convert_time_list_to_big_ints(validated_data["avaliable_slots"])
        del validated_data["avaliable_slots"], validated_data["interviewee"]
        print(validated_data)
        IntervieweeAvaliableTimeSlots.objects.filter(
            interviewee_id=validated_data["interviewee_id"],
            available_date=validated_data["available_date"],
        ).update(**validated_data)
        return None
