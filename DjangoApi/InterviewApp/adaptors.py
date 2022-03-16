def convert_time_list_to_big_ints(time_slot_list):
    """
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    """
    time_slot_list = list(set(time_slot_list))
    for index, time_slot in enumerate(time_slot_list):
        if time_slot == 0:
            time_slot_list[index] = 24
    if len(time_slot_list) > 12:
        time_slot_list1 = time_slot_list[:12]
        ipayload1 = time_slot_list1.pop(0)
        for i in time_slot_list1:
            ipayload1 = (ipayload1 << 5) + i
        time_slot_list2 = time_slot_list[12:]
        ipayload2 = time_slot_list2.pop(0)
        for i in time_slot_list2:
            ipayload2 = (ipayload2 << 5) + i
        return ipayload1, ipayload2
    elif len(time_slot_list) > 0:
        ipayload = time_slot_list.pop(0)
        for i in time_slot_list:
            ipayload = (ipayload << 5) + i
        return ipayload, 0
    else:
        return 0, 0


def convert_big_ints_to_time_list(ipayload1, ipayload2):
    time_slot_list = []
    while ipayload1 > 0:
        time_slot = ipayload1 - ((ipayload1 >> 5) << 5)
        time_slot = 0 if time_slot == 24 else time_slot
        time_slot_list.append(time_slot)
        ipayload1 = ipayload1 >> 5
    while ipayload2 > 0:
        time_slot = ipayload2 - ((ipayload2 >> 5) << 5)
        time_slot = 0 if time_slot == 24 else time_slot
        time_slot_list.append(time_slot)
        ipayload2 = ipayload2 >> 5
    return time_slot_list


def filter_response_data(slots_serializer_data, user_type):
    slot_data_list = []
    for slot_data in slots_serializer_data:
        already_exist = False
        for slot_data_item in slot_data_list:
            if slot_data[user_type]["id"] == slot_data_item[user_type]["id"]:
                already_exist = True
                break

        if already_exist:
            slot_data_item["avaliable_slots"].append(
                {slot_data["available_date"]: slot_data["avaliable_slots"]}
            )
        else:
            slot_data_item = {}
            slot_data_item[user_type] = slot_data[user_type]
            slot_data_item["avaliable_slots"] = [
                {slot_data["available_date"]: slot_data["avaliable_slots"]}
            ]
            slot_data_list.append(slot_data_item)
    return slot_data_list


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def convert_to_time(slot_time_list):
    slot_time_list.sort()
    slot_time_list_map = {
        0: "12 am to 01 am",
        1: "01 am to 02 am",
        2: "02 am to 03 am",
        3: "03 am to 04 am",
        4: "04 am to 05 am",
        5: "05 am to 06 am",
        6: "06 am to 07 am",
        7: "07 am to 08 am",
        8: "08 am to 09 am",
        9: "09 am to 10 am",
        10: "10 am to 11 am",
        11: "11 am to 12 am",
        12: "12 pm to 01 pm",
        13: "01 pm to 02 pm",
        14: "02 pm to 03 pm",
        15: "03 pm to 04 pm",
        16: "04 pm to 05 pm",
        17: "05 pm to 06 pm",
        18: "06 pm to 07 pm",
        19: "07 pm to 08 pm",
        20: "08 pm to 09 pm",
        21: "09 pm to 10 pm",
        22: "10 pm to 11 pm",
        23: "11 pm to 12 am",
    }
    formated_slot_time_list = []
    for slot_time in slot_time_list:
        formated_slot_time_list.append(slot_time_list_map[slot_time])
    return formated_slot_time_list
