from django.http import JsonResponse
from InterviewApp.utils import CURD_FUNCTIONS_MAPPING, find_avaliable_interview_slots
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','PUT','POST','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def interviewer(request, record_id=None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split("/")[1]](
        request, record_id
    )
    if type(return_data) is dict and return_data.get("status"):
        return JsonResponse(return_data, safe=False, status=return_data.pop("status"))
    return JsonResponse(return_data, safe=False)


@api_view(['GET','PUT','POST','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def interviewee(request, record_id=None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split("/")[1]](
        request, record_id
    )
    if type(return_data) is dict and return_data.get("status"):
        return JsonResponse(return_data, safe=False, status=return_data.pop("status"))
    return JsonResponse(return_data, safe=False)


@api_view(['GET','PUT','POST','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def interviewer_slot(request, interviewer_id=None, year=None, month=None, day=None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split("/")[1]](
        request, interviewer_id, (year, month, day)
    )
    if type(return_data) is dict and return_data.get("status"):
        return JsonResponse(return_data, safe=False, status=return_data.pop("status"))
    return JsonResponse(return_data, safe=False)


@api_view(['GET','PUT','POST','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def interviewee_slot(request, interviewee_id=None, year=None, month=None, day=None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split("/")[1]](
        request, interviewee_id, (year, month, day)
    )
    if type(return_data) is dict and return_data.get("status"):
        return JsonResponse(return_data, safe=False, status=return_data.pop("status"))
    return JsonResponse(return_data, safe=False)

@api_view()
@permission_classes([IsAuthenticated])
def find_available_slots(request):
    return_data = find_avaliable_interview_slots(request)
    return JsonResponse(return_data, safe=False)
