from django.http import JsonResponse
from InterviewApp.utils import CURD_FUNCTIONS_MAPPING,find_avaliable_interview_slots
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def interviewer(request,record_id =None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split('/')[1]](request,record_id)
    return JsonResponse(return_data,safe=False)

@csrf_exempt
def interviewee(request,record_id =None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split('/')[1]](request,record_id)
    return JsonResponse(return_data,safe=False)

@csrf_exempt
def interviewer_slot(request,record_id =None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split('/')[1]](request,record_id)
    return JsonResponse(return_data,safe=False)

@csrf_exempt
def interviewee_slot(request,record_id =None):
    return_data = CURD_FUNCTIONS_MAPPING[request.method][request.path.split('/')[1]](request,record_id)
    return JsonResponse(return_data,safe=False)

@csrf_exempt
def find_available_slots(request):
    return_data = find_avaliable_interview_slots(request)
    return JsonResponse(return_data,safe=False)