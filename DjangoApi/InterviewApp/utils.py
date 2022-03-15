from django.db.models import Q
from rest_framework.parsers import JSONParser
from InterviewApp.models import  (
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
from datetime import datetime, timedelta
_interviewer_url_path = 'interviewer'
_interviewee_url_path = 'interviewee'
_interviewer_slot_url_path = 'interviewer-slot'
_interviewee_slot_url_path = 'interviewee-slot'

def get_interviewer_function(request,user_id):
    if user_id:
        try:
            interviewer = Interviewer.objects.get(id = user_id)
            interviewer_serializer = InterviewerSerializer(interviewer)
            return interviewer_serializer.data
        except Interviewer.DoesNotExist:
            return "Record doesn't exist"
    else:
        interviewers = Interviewer.objects.all()
        interviewers_serializer = InterviewerSerializer(interviewers,many=True)
        return interviewers_serializer.data
        
def post_interviewer_function(request,user_id):
    interviewer_data = JSONParser().parse(request)
    interviewer_serializer = InterviewerSerializer(data = interviewer_data)
    if interviewer_serializer.is_valid():
        interviewer_serializer.save()
        return interviewer_serializer.data
    return interviewer_serializer.errors

def put_interviewer_function(request,user_id):
    interviewer_data = JSONParser().parse(request)
    try:
        interviewer = Interviewer.objects.get(id = user_id)
    except Interviewer.DoesNotExist:
        return "Record doesn't exist"
    interviewer_serializer = InterviewerSerializer(interviewer,data=interviewer_data)
    if interviewer_serializer.is_valid():
        interviewer_serializer.save()
        return interviewer_serializer.data
    return interviewer_serializer.errors

def patch_interviewer_function(request,user_id):
    interviewer_data = JSONParser().parse(request)
    try:
        interviewer = Interviewer.objects.get(id = user_id)
    except Interviewer.DoesNotExist:
        return "Record doesn't exist"
    interviewer_serializer = InterviewerSerializer(interviewer,data=interviewer_data,partial=True)
    if interviewer_serializer.is_valid():
        interviewer_serializer.save()
        return interviewer_serializer.data
    return interviewer_serializer.errors

def delete_interviewer_function(request,user_id):
    try:
        interviewer = Interviewer.objects.get(id = user_id)
        interviewer.delete()
    except Interviewer.DoesNotExist:
        return "Record doesn't exist"
    return "record deleted successfully"

def get_interviewee_function(request,user_id):
    if user_id:
        try:
            interviewee = Interviewee.objects.get(id = user_id)
            interviewee_serializer = IntervieweeSerializer(interviewee)
            return interviewee_serializer.data
        except Interviewee.DoesNotExist:
            return "Record doesn't exist"
    else:
        interviewees = Interviewee.objects.all()
        interviewees_serializer = IntervieweeSerializer(interviewees,many=True)
        return interviewees_serializer.data
        
def post_interviewee_function(request,user_id):
    interviewee_data = JSONParser().parse(request)
    interviewee_serializer = IntervieweeSerializer(data = interviewee_data)
    if interviewee_serializer.is_valid():
        interviewee_serializer.save()
        return interviewee_serializer.data
    return interviewee_serializer.errors

def put_interviewee_function(request,user_id):
    interviewee_data = JSONParser().parse(request)
    try:
        interviewee = Interviewee.objects.get(id = user_id)
    except Interviewee.DoesNotExist:
        return "Record doesn't exist"
    interviewee_serializer = IntervieweeSerializer(interviewee,data=interviewee_data)
    if interviewee_serializer.is_valid():
        interviewee_serializer.save()
        return interviewee_serializer.data
    return interviewee_serializer.errors

def patch_interviewee_function(request,user_id):
    interviewee_data = JSONParser().parse(request)
    try:
        interviewee = Interviewee.objects.get(id = user_id)
    except Interviewee.DoesNotExist:
        return "Record doesn't exist"
    interviewee_serializer = IntervieweeSerializer(interviewee,data=interviewee_data,partial=True)
    if interviewee_serializer.is_valid():
        interviewee_serializer.save()
        return interviewee_serializer.data
    return interviewee_serializer.errors

def delete_interviewee_function(request,user_id):
    try:
        interviewee = Interviewee.objects.get(id = user_id)
        interviewee.delete()
    except Interviewee.DoesNotExist:
        return "Record doesn't exist"
    return "record deleted successfully"

def get_interviewer_slot_function(request,record_id):
    if record_id:
        try:
            interviewer_slot = InterviewerAvaliableTimeSlots.objects.get(id = record_id)
            interviewer_slot_serializer = InterviewerSlotQuerySerializer(interviewer_slot)
            interviewer_slots_serializer_data = [interviewer_slot_serializer.data]
        except InterviewerAvaliableTimeSlots.DoesNotExist:
            return "Record doesn't exist"
    elif request.GET.get('interviewer_id') or request.GET.get('interviewer_name') or request.GET.get('interviewer_email'):
        try:
            custom_query = Q(interviewer_id = request.GET.get('interviewer_id'))| Q(interviewer__name = request.GET.get('interviewer_name')) | Q(interviewer__email = request.GET.get('interviewer_email'))
            interviewer_slots = InterviewerAvaliableTimeSlots.objects.filter(custom_query)
            interviewer_slots_serializer = InterviewerSlotQuerySerializer(interviewer_slots,many=True)
            interviewer_slots_serializer_data = interviewer_slots_serializer.data
        except InterviewerAvaliableTimeSlots.DoesNotExist:
            return "Record doesn't exist"
    else:
        interviewer_slots = InterviewerAvaliableTimeSlots.objects.all()
        interviewer_slots_serializer = InterviewerSlotQuerySerializer(interviewer_slots,many=True)
        interviewer_slots_serializer_data = interviewer_slots_serializer.data
    return filter_response_data(interviewer_slots_serializer_data,_interviewer_url_path)

def post_interviewer_slot_function(request,record_id):
    interviewer_slot_data = JSONParser().parse(request)
    interviewer_slot_serializer = InterviewerSlotMutateSerializer(data = interviewer_slot_data)
    if interviewer_slot_serializer.is_valid():
        interviewer_slot_serializer.save()
        return interviewer_slot_serializer.data
    return interviewer_slot_serializer.errors

def put_interviewer_slot_function(request,record_id):
    interviewer_slot_data = JSONParser().parse(request)
    try:
        interviewer_slot = InterviewerAvaliableTimeSlots.objects.get(id = record_id)
    except InterviewerAvaliableTimeSlots.DoesNotExist:
        return "Record doesn't exist"
    interviewer_slot_serializer = InterviewerSlotMutateSerializer(interviewer_slot,data=interviewer_slot_data)
    if interviewer_slot_serializer.is_valid():
        interviewer_slot_serializer.save()
        return interviewer_slot_serializer.data
    return interviewer_slot_serializer.errors

def patch_interviewer_slot_function(request,record_id):
    interviewer_slot_data = JSONParser().parse(request)
    try:
        interviewer_slot = InterviewerAvaliableTimeSlots.objects.get(id = record_id)
    except InterviewerAvaliableTimeSlots.DoesNotExist:
        return "Record doesn't exist"
    interviewer_slot_serializer = InterviewerSlotMutateSerializer(interviewer_slot,data=interviewer_slot_data,partial=True)
    if interviewer_slot_serializer.is_valid():
        interviewer_slot_serializer.save()
        return interviewer_slot_serializer.data
    return interviewer_slot_serializer.errors

def delete_interviewer_slot_function(request,record_id):
    print("asdsadsads")
    try:
        if record_id:
            interviewer_slot = InterviewerAvaliableTimeSlots.objects.get(id = record_id)
            interviewer_slot.delete()
        elif request.GET.get('interviewer_id'):
            print("asdasdasd")
            interviewer_slots = InterviewerAvaliableTimeSlots.objects.filter(interviewer_id = request.GET.get('interviewer_id'))
            interviewer_slots.delete()
        else:
            return "please enter the record id in url or add the interviewer's id as interviewer_id params"
    except InterviewerAvaliableTimeSlots.DoesNotExist:
        return "Record doesn't exist"
    return "record deleted successfully"

def get_interviewee_slot_function(request,record_id):
    if record_id:
        try:
            interviewee_slot = IntervieweeAvaliableTimeSlots.objects.get(id = record_id)
            interviewee_slot_serializer = IntervieweeSlotQuerySerializer(interviewee_slot)
            interviewee_slots_serializer_data = [interviewee_slot_serializer.data]
        except IntervieweeAvaliableTimeSlots.DoesNotExist:
            return "Record doesn't exist"
    elif request.GET.get('interviewee_id') or request.GET.get('interviewee_name') or request.GET.get('interviewee_email'):
        try:
            custom_query = Q(interviewee_id = request.GET.get('interviewee_id'))| Q(interviewee__name = request.GET.get('interviewee_name')) | Q(interviewee__email = request.GET.get('interviewee_email'))
            interviewee_slots = IntervieweeAvaliableTimeSlots.objects.filter(custom_query)
            interviewee_slots_serializer = IntervieweeSlotQuerySerializer(interviewee_slots,many=True)
            interviewee_slots_serializer_data = interviewee_slots_serializer.data
        except IntervieweeAvaliableTimeSlots.DoesNotExist:
            return "Record doesn't exist"
    else:
        interviewee_slots = IntervieweeAvaliableTimeSlots.objects.all()
        interviewee_slots_serializer = IntervieweeSlotQuerySerializer(interviewee_slots,many=True)
        interviewee_slots_serializer_data = interviewee_slots_serializer.data
    return filter_response_data(interviewee_slots_serializer_data,_interviewee_url_path)

def post_interviewee_slot_function(request,record_id):
    interviewee_slot_data = JSONParser().parse(request)
    interviewee_slot_serializer = IntervieweeSlotMutateSerializer(data = interviewee_slot_data)
    if interviewee_slot_serializer.is_valid():
        interviewee_slot_serializer.save()
        return interviewee_slot_serializer.data
    return interviewee_slot_serializer.errors

def put_interviewee_slot_function(request,record_id):
    interviewee_slot_data = JSONParser().parse(request)
    try:
        interviewee_slot = IntervieweeAvaliableTimeSlots.objects.get(id = record_id)
    except IntervieweeAvaliableTimeSlots.DoesNotExist:
        return "Record doesn't exist"
    interviewee_slot_serializer = IntervieweeSlotMutateSerializer(interviewee_slot,data=interviewee_slot_data)
    if interviewee_slot_serializer.is_valid():
        interviewee_slot_serializer.save()
        return interviewee_slot_serializer.data
    return interviewee_slot_serializer.errors

def patch_interviewee_slot_function(request,record_id):
    interviewee_slot_data = JSONParser().parse(request)
    try:
        interviewee_slot = IntervieweeAvaliableTimeSlots.objects.get(id = record_id)
    except IntervieweeAvaliableTimeSlots.DoesNotExist:
        return "Record doesn't exist"
    interviewee_slot_serializer = IntervieweeSlotMutateSerializer(interviewee_slot,data=interviewee_slot_data,partial=True)
    if interviewee_slot_serializer.is_valid():
        interviewee_slot_serializer.save()
        return interviewee_slot_serializer.data
    return interviewee_slot_serializer.errors

def delete_interviewee_slot_function(request,record_id):
    print("asdsadsads")
    try:
        if record_id:
            interviewee_slot = IntervieweeAvaliableTimeSlots.objects.get(id = record_id)
            interviewee_slot.delete()
        elif request.GET.get('interviewee_id'):
            print("asdasdasd")
            interviewee_slots = IntervieweeAvaliableTimeSlots.objects.filter(interviewee_id = request.GET.get('interviewee_id'))
            interviewee_slots.delete()
        else:
            return "please enter the record id in url or add the interviewee's id as interviewee_id params"
    except IntervieweeAvaliableTimeSlots.DoesNotExist:
        return "Record doesn't exist"
    return "record deleted successfully"

CURD_FUNCTIONS_MAPPING = {
    "GET": {
        _interviewer_url_path: get_interviewer_function,
        _interviewee_url_path: get_interviewee_function,
        _interviewer_slot_url_path: get_interviewer_slot_function,
        _interviewee_slot_url_path: get_interviewee_slot_function,
    } ,
    "POST": {
        _interviewer_url_path : post_interviewer_function,
        _interviewee_url_path : post_interviewee_function,
        _interviewer_slot_url_path : post_interviewer_slot_function,
        _interviewee_slot_url_path : post_interviewee_slot_function,
    },
    "PUT": {
        _interviewer_url_path  : put_interviewer_function,
        _interviewee_url_path  : put_interviewee_function,
        _interviewer_slot_url_path  : put_interviewer_slot_function,
        _interviewee_slot_url_path  : put_interviewee_slot_function
    },
    "PATCH": {
        _interviewer_url_path  : patch_interviewer_function,
        _interviewee_url_path  : patch_interviewee_function,
        _interviewer_slot_url_path : patch_interviewer_slot_function,
        _interviewee_slot_url_path : patch_interviewee_slot_function,
    } ,
    "DELETE": {
        _interviewer_url_path  : delete_interviewer_function,
        _interviewee_url_path  : delete_interviewee_function,
        _interviewer_slot_url_path : delete_interviewer_slot_function,
        _interviewee_slot_url_path : delete_interviewee_slot_function,
    },
}

def filter_response_data(slots_serializer_data,user_type):
    slot_data_list = []
    for slot_data in slots_serializer_data:
        already_exist = False
        for slot_data_item in slot_data_list:
            if slot_data_item[f'{user_type}_id'] == slot_data[user_type]['id'] and slot_data_item[f'{user_type}_name'] == slot_data[user_type]['name'] and slot_data_item[f'{user_type}_email'] == slot_data[user_type]['email']:
                already_exist = True
                break
        if already_exist:
            slot_data_item['slot_list'].append({'record_id':slot_data['id'],'start_time':slot_data['start_time'],'end_time':slot_data['end_time']})
        else:
            slot_data_item = {}
            slot_data_item[f'{user_type}_id'] = slot_data[user_type]['id']
            slot_data_item[f'{user_type}_name'] = slot_data[user_type]['name']
            slot_data_item[f'{user_type}_email'] = slot_data[user_type]['email']
            slot_data_item['slot_list'] = [{'record_id':slot_data['id'],'start_time':slot_data['start_time'],'end_time':slot_data['end_time']}]
            slot_data_list.append(slot_data_item)
    return slot_data_list

def find_avaliable_interview_slots(request):
    if request.method != 'GET':
        return "method not allowed"
    interviewer_id = request.GET.get('interviewer_id')
    interviewee_id = request.GET.get('interviewee_id')
    interviewer_slots = InterviewerAvaliableTimeSlots.objects.filter(interviewer_id = interviewer_id).order_by('start_time').values('start_time','end_time')
    interviewee_slots = IntervieweeAvaliableTimeSlots.objects.filter(interviewee_id = interviewee_id).order_by('start_time').values('start_time','end_time')
    interviewer_slot_dict = find_slot_data(interviewer_slots)
    print(interviewer_slot_dict)
    combined_slots = find_slot_data(interviewee_slots,interviewer_slot_dict)
    return combined_slots

def find_slot_data(slot_data_list,interviewer_slots =False):
    slot_data_dict = {}
    for slot_data in slot_data_list:
        start_time = slot_data['start_time']
        start_date = str(start_time.date())
        if start_time.minute >0: #finding the next whole hour
            start_hour = (start_time + timedelta(hours=1)).hour
            if start_hour == 0: #finding the next day
                start_date = str((start_time + timedelta(days=1)).date())
        else:
            start_hour = start_time.hour
        end_time = slot_data['end_time']
        end_date = str(end_time.date())
        if end_time.minute >0: #finding the previous whole hour
            end_hour = (end_time - timedelta(hours=1)).hour
        else:
            end_hour = end_time.hour
        if end_hour == 0: #for solving issues with range alocation
            end_hour = 24
            end_date = str((end_time - timedelta(days=1)).date())
        while True:
            if interviewer_slots:
                if start_date not in interviewer_slots.keys():
                    if start_date == end_date:
                        break
                    else:
                        continue
            if start_date == end_date:
                if start_date in slot_data_dict:
                    slot_data_dict[start_date] =list(set(slot_data_dict[start_date]) | set(range(start_hour,end_hour)))
                else:
                    slot_data_dict[start_date] = list(range(start_hour,end_hour))
                break
            else:
                if start_date in slot_data_dict:
                    slot_data_dict[start_date] =list(set(slot_data_dict[start_date]) | set(range(start_hour,24)))
                else:
                    slot_data_dict[start_date] = list(range(start_hour,24))
                start_date = str((datetime.strptime(start_date,'%Y-%m-%d')+ timedelta(days=1)).date())
                start_hour = 0
    return slot_data_dict
    
