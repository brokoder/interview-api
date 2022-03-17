from urllib import response
from django.db.models import Q
from rest_framework.parsers import JSONParser
from InterviewApp.models import (
    Interviewer,
    Interviewee,
    InterviewerAvaliableTimeSlots,
    IntervieweeAvaliableTimeSlots,
)
from InterviewApp.serializer import (
    InterviewerSerializer,
    IntervieweeSerializer,
    InterviewerSlotQuerySerializer,
    InterviewerSlotMutateSerializer,
    IntervieweeSlotQuerySerializer,
    IntervieweeSlotMutateSerializer,
)

# from InterviewApp.serializer import InterviewerSlotSerializer
from django.db import connection
from InterviewApp.adaptors import (
    convert_big_ints_to_time_list,
    filter_response_data,
    dictfetchall,
    convert_to_time,
)

_interviewer_url_path = "interviewer"
_interviewee_url_path = "interviewee"
_interviewer_slot_url_path = "interviewer-slot"
_interviewee_slot_url_path = "interviewee-slot"


def get_interviewer_function(request, user_id):
    if user_id:
        try:
            interviewer = Interviewer.objects.get(id=user_id)
            interviewer_serializer = InterviewerSerializer(interviewer)
            return interviewer_serializer.data
        except Interviewer.DoesNotExist:
            return {"error": "Record doesn't exist", "status": 404}
    else:
        interviewers = Interviewer.objects.all()
        interviewers_serializer = InterviewerSerializer(interviewers, many=True)
        return interviewers_serializer.data


def post_interviewer_function(request, user_id):
    interviewer_data = JSONParser().parse(request)
    interviewer_serializer = InterviewerSerializer(data=interviewer_data)
    if interviewer_serializer.is_valid():
        interviewer_serializer.save()
        return interviewer_serializer.data
    return interviewer_serializer.errors


def put_interviewer_function(request, user_id):
    interviewer_data = JSONParser().parse(request)
    try:
        interviewer = Interviewer.objects.get(id=user_id)
    except Interviewer.DoesNotExist:
        return {"error": "Record doesn't exist", "status": 404}
    interviewer_serializer = InterviewerSerializer(interviewer, data=interviewer_data)
    if interviewer_serializer.is_valid():
        interviewer_serializer.save()
        return interviewer_serializer.data
    return interviewer_serializer.errors


def patch_interviewer_function(request, user_id):
    interviewer_data = JSONParser().parse(request)
    try:
        interviewer = Interviewer.objects.get(id=user_id)
    except Interviewer.DoesNotExist:
        return {"error": "Record doesn't exist", "status": 404}
    interviewer_serializer = InterviewerSerializer(
        interviewer, data=interviewer_data, partial=True
    )
    if interviewer_serializer.is_valid():
        interviewer_serializer.save()
        return interviewer_serializer.data
    return interviewer_serializer.errors


def delete_interviewer_function(request, user_id):
    try:
        interviewer = Interviewer.objects.get(id=user_id)
        interviewer.delete()
    except Interviewer.DoesNotExist:
        return {"error": "Record doesn't exist", "status": 404}
    return {"message": "Record deleted successfully"}


def get_interviewee_function(request, user_id):
    if user_id:
        try:
            interviewee = Interviewee.objects.get(id=user_id)
            interviewee_serializer = IntervieweeSerializer(interviewee)
            return interviewee_serializer.data
        except Interviewee.DoesNotExist:
            return {"error": "Record doesn't exist", "status": 404}
    else:
        interviewees = Interviewee.objects.all()
        interviewees_serializer = IntervieweeSerializer(interviewees, many=True)
        return interviewees_serializer.data


def post_interviewee_function(request, user_id):
    interviewee_data = JSONParser().parse(request)
    interviewee_serializer = IntervieweeSerializer(data=interviewee_data)
    if interviewee_serializer.is_valid():
        interviewee_serializer.save()
        return interviewee_serializer.data
    return interviewee_serializer.errors


def put_interviewee_function(request, user_id):
    interviewee_data = JSONParser().parse(request)
    try:
        interviewee = Interviewee.objects.get(id=user_id)
    except Interviewee.DoesNotExist:
        return {"error": "Record doesn't exist", "status": 404}
    interviewee_serializer = IntervieweeSerializer(interviewee, data=interviewee_data)
    if interviewee_serializer.is_valid():
        interviewee_serializer.save()
        return interviewee_serializer.data
    return interviewee_serializer.errors


def patch_interviewee_function(request, user_id):
    interviewee_data = JSONParser().parse(request)
    try:
        interviewee = Interviewee.objects.get(id=user_id)
    except Interviewee.DoesNotExist:
        return {"error": "Record doesn't exist", "status": 404}
    interviewee_serializer = IntervieweeSerializer(
        interviewee, data=interviewee_data, partial=True
    )
    if interviewee_serializer.is_valid():
        interviewee_serializer.save()
        return interviewee_serializer.data
    return interviewee_serializer.errors


def delete_interviewee_function(request, user_id):
    try:
        interviewee = Interviewee.objects.get(id=user_id)
        interviewee.delete()
    except Interviewee.DoesNotExist:
        return {"error": "Record doesn't exist", "status": 404}
    return {"message": "Record deleted successfully"}


def get_interviewer_slot_function(request, interviewer_id, date_set):
    custom_query = Q()
    if interviewer_id and interviewer_id != "all":
        custom_query = custom_query & Q(interviewer_id=interviewer_id)
    if date_set[0]:
        custom_query = custom_query & Q(available_date__year=date_set[0])
    if date_set[1]:
        custom_query = custom_query & Q(available_date__month=date_set[1])
    if date_set[2]:
        custom_query = custom_query & Q(available_date__day=date_set[2])
    interviewer_slot = InterviewerAvaliableTimeSlots.objects.filter(custom_query)
    interviewer_slots_serializer = InterviewerSlotQuerySerializer(
        interviewer_slot, many=True
    )
    response_data_list = interviewer_slots_serializer.data
    for response_data in response_data_list:
        response_data["avaliable_slots"] = convert_big_ints_to_time_list(
            response_data["ipayload1"], response_data["ipayload2"]
        )
        del response_data["ipayload1"], response_data["ipayload2"]
    return filter_response_data(response_data_list, _interviewer_url_path)


def post_interviewer_slot_function(request, interviewer_id, date_data):
    interviewer_slot_data = JSONParser().parse(request)
    interviewer_slot_serializer = InterviewerSlotMutateSerializer(
        data=interviewer_slot_data
    )
    if interviewer_slot_serializer.is_valid():
        if InterviewerAvaliableTimeSlots.objects.filter(
            interviewer_id=interviewer_slot_data["interviewer"],
            available_date=interviewer_slot_data["available_date"],
        ).exists():
            return {
                "error": "Record of same interviewer for the same date already exists choose put or patch method to update the current record",
                "status": 409,
            }
        interviewer_slot_serializer.create(
            validated_data=interviewer_slot_serializer.data
        )
        return interviewer_slot_serializer.data
    return interviewer_slot_serializer.errors


def put_interviewer_slot_function(request, interviewer_id, date_set):
    interviewer_slot_data = JSONParser().parse(request)
    interviewer_slot_serializer = InterviewerSlotMutateSerializer(
        data=interviewer_slot_data
    )
    if interviewer_slot_serializer.is_valid():
        interviewer_slot_serializer.update(
            validated_data=interviewer_slot_serializer.data
        )
        return interviewer_slot_serializer.data
    return interviewer_slot_serializer.errors


def patch_interviewer_slot_function(request, interviewer_id, date_set):
    interviewer_slot_data = JSONParser().parse(request)
    interviewer_slot_serializer = InterviewerSlotMutateSerializer(
        data=interviewer_slot_data, partial=True
    )
    if interviewer_slot_serializer.is_valid():
        interviewer_slot_serializer.update(
            validated_data=interviewer_slot_serializer.data
        )
        return interviewer_slot_serializer.data
    return interviewer_slot_serializer.errors


def delete_interviewer_slot_function(request, interviewer_id, date_set):
    custom_query = Q()
    if interviewer_id and interviewer_id != "all":
        custom_query = custom_query & Q(interviewer_id=interviewer_id)
    if date_set[0]:
        custom_query = custom_query & Q(available_date__year=date_set[0])
    if date_set[1]:
        custom_query = custom_query & Q(available_date__month=date_set[1])
    if date_set[2]:
        custom_query = custom_query & Q(available_date__day=date_set[2])
    interviewer_slots = InterviewerAvaliableTimeSlots.objects.filter(custom_query)
    delete_count, _ = interviewer_slots.delete()
    if delete_count:
        return {"message": "Record deleted successfully"}
    return {"error": "Record doesn't exist", "status": 404}

def get_interviewee_slot_function(request, interviewee_id, date_set):
    custom_query = Q()
    if interviewee_id and interviewee_id != "all":
        custom_query = custom_query & Q(interviewee_id=interviewee_id)
    if date_set[0]:
        custom_query = custom_query & Q(available_date__year=date_set[0])
    if date_set[1]:
        custom_query = custom_query & Q(available_date__month=date_set[1])
    if date_set[2]:
        custom_query = custom_query & Q(available_date__day=date_set[2])
    interviewee_slot = IntervieweeAvaliableTimeSlots.objects.filter(custom_query)
    interviewee_slots_serializer = IntervieweeSlotQuerySerializer(
        interviewee_slot, many=True
    )
    response_data_list = interviewee_slots_serializer.data
    for response_data in response_data_list:
        response_data["avaliable_slots"] = convert_big_ints_to_time_list(
            response_data["ipayload1"], response_data["ipayload2"]
        )
        del response_data["ipayload1"], response_data["ipayload2"]
    return filter_response_data(response_data_list, _interviewee_url_path)


def post_interviewee_slot_function(request, interviewee_id, date_data):
    interviewee_slot_data = JSONParser().parse(request)
    if IntervieweeAvaliableTimeSlots.objects.filter(
        interviewee_id=interviewee_slot_data["interviewee"],
        available_date=interviewee_slot_data["available_date"],
    ).exists():
        return {
            "message": "Record of same interviewee for the same date already exists choose put or patch method to update the current record",
            "status": 400,
        }
    interviewee_slot_serializer = IntervieweeSlotMutateSerializer(
        data=interviewee_slot_data
    )
    if interviewee_slot_serializer.is_valid():
        interviewee_slot_serializer.create(
            validated_data=interviewee_slot_serializer.data
        )
        return interviewee_slot_serializer.data
    return interviewee_slot_serializer.errors


def put_interviewee_slot_function(request, interviewee_id, date_set):
    interviewee_slot_data = JSONParser().parse(request)
    interviewee_slot_serializer = IntervieweeSlotMutateSerializer(
        data=interviewee_slot_data
    )
    if interviewee_slot_serializer.is_valid():
        interviewee_slot_serializer.update(
            validated_data=interviewee_slot_serializer.data
        )
        return interviewee_slot_serializer.data
    return interviewee_slot_serializer.errors


def patch_interviewee_slot_function(request, interviewee_id, date_set):
    interviewee_slot_data = JSONParser().parse(request)
    interviewee_slot_serializer = IntervieweeSlotMutateSerializer(
        data=interviewee_slot_data, partial=True
    )
    if interviewee_slot_serializer.is_valid():
        interviewee_slot_serializer.update(
            validated_data=interviewee_slot_serializer.data
        )
        return interviewee_slot_serializer.data
    return interviewee_slot_serializer.errors


def delete_interviewee_slot_function(request, interviewee_id, date_set):
    custom_query = Q()
    if interviewee_id and interviewee_id != "all":
        custom_query = custom_query & Q(interviewee_id=interviewee_id)
    if date_set[0]:
        custom_query = custom_query & Q(available_date__year=date_set[0])
    if date_set[1]:
        custom_query = custom_query & Q(available_date__month=date_set[1])
    if date_set[2]:
        custom_query = custom_query & Q(available_date__day=date_set[2])
    interviewee_slots = IntervieweeAvaliableTimeSlots.objects.filter(custom_query)
    delete_count, _ = interviewee_slots.delete()
    if delete_count:
        return {"message": "Record deleted successfully"}
    return {"error": "Record doesn't exist", "status": 404}


CURD_FUNCTIONS_MAPPING = {
    "GET": {
        _interviewer_url_path: get_interviewer_function,
        _interviewee_url_path: get_interviewee_function,
        _interviewer_slot_url_path: get_interviewer_slot_function,
        _interviewee_slot_url_path: get_interviewee_slot_function,
    },
    "POST": {
        _interviewer_url_path: post_interviewer_function,
        _interviewee_url_path: post_interviewee_function,
        _interviewer_slot_url_path: post_interviewer_slot_function,
        _interviewee_slot_url_path: post_interviewee_slot_function,
    },
    "PUT": {
        _interviewer_url_path: put_interviewer_function,
        _interviewee_url_path: put_interviewee_function,
        _interviewer_slot_url_path: put_interviewer_slot_function,
        _interviewee_slot_url_path: put_interviewee_slot_function,
    },
    "PATCH": {
        _interviewer_url_path: patch_interviewer_function,
        _interviewee_url_path: patch_interviewee_function,
        _interviewer_slot_url_path: patch_interviewer_slot_function,
        _interviewee_slot_url_path: patch_interviewee_slot_function,
    },
    "DELETE": {
        _interviewer_url_path: delete_interviewer_function,
        _interviewee_url_path: delete_interviewee_function,
        _interviewer_slot_url_path: delete_interviewer_slot_function,
        _interviewee_slot_url_path: delete_interviewee_slot_function,
    },
}


def find_avaliable_interview_slots(request):
    interviewer_id = request.GET.get("interviewer")
    interviewee_id = request.GET.get("interviewee")
    query_str = """
        SELECT
            InterviewApp_intervieweravaliabletimeslots.interviewer_id,
            InterviewApp_intervieweeavaliabletimeslots.interviewee_id,
            InterviewApp_intervieweravaliabletimeslots.available_date as interviewer_available_date,
            InterviewApp_intervieweeavaliabletimeslots.available_date as interviewee_available_date,
            InterviewApp_intervieweravaliabletimeslots.ipayload1 as interviewer_ipayload1,
            InterviewApp_intervieweravaliabletimeslots.ipayload2 as interviewer_ipayload2,
            InterviewApp_intervieweeavaliabletimeslots.ipayload1 as interviewee_ipayload1,
            InterviewApp_intervieweeavaliabletimeslots.ipayload2 as interviewee_ipayload2
        FROM
            InterviewApp_intervieweravaliabletimeslots
            INNER JOIN InterviewApp_intervieweeavaliabletimeslots
                ON InterviewApp_intervieweravaliabletimeslots.available_date = InterviewApp_intervieweeavaliabletimeslots.available_date
                    AND InterviewApp_intervieweravaliabletimeslots.interviewer_id = {}
                    AND InterviewApp_intervieweeavaliabletimeslots.interviewee_id = {};
        """.format(
        interviewer_id, interviewee_id
    )
    with connection.cursor() as cursor:
        cursor.execute(query_str)
        common_slots_data_list = dictfetchall(cursor)
    if not common_slots_data_list:
        return "No common records found"
    total_common_time_slots_data = {}
    total_common_time_slots_data["interviewer"] = interviewer_id
    total_common_time_slots_data["interviewee"] = interviewee_id
    total_common_time_slots_data["avaliable_slots"] = []
    for common_slots_data in common_slots_data_list:
        common_slots_data[
            "interviewer_available_slots"
        ] = convert_big_ints_to_time_list(
            common_slots_data["interviewer_ipayload1"],
            common_slots_data["interviewer_ipayload2"],
        )
        common_slots_data[
            "interviewee_available_slots"
        ] = convert_big_ints_to_time_list(
            common_slots_data["interviewee_ipayload1"],
            common_slots_data["interviewee_ipayload2"],
        )
        common_time_slots_data = {}
        common_available_slots = list(
            set(common_slots_data["interviewee_available_slots"])
            & set(common_slots_data["interviewer_available_slots"])
        )
        common_time_slots_data[
            str(common_slots_data["interviewee_available_date"])
        ] = convert_to_time(common_available_slots)
        total_common_time_slots_data["avaliable_slots"].append(common_time_slots_data)
    return total_common_time_slots_data
