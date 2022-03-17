# Interview Scheduler Api

## Summary
Scheduling interviews is a burden in most companies. When you want to schedule multiple interviews in a single day, it depends on the availability of the interviewer and the candidate. 
By using this api system we can:
    1. CURD records for Interviewers
    2. CURD records for Interviewees
    3. CURD records of avalilable slots for Interviewers
    4. CURD records of avalilable slots for Interviewees
    5. Get the avalilable slots common for a interviewer and interviewee
Framework used - Django rest framework
Database used - Sqlite
Programming language - python

## Api breakdown
### Interviewer
Api for Interviewer resource is `Interviewer`
Fields for Api are 
1. name - Name of the Interviewer 
2. email - Email of the Interviewer. Unique feild, value should 
be of email format
Supported operations are `GET`,`POST`,`PUT`,`PATCH`,`DELETE`.
#### GET
1. Use `Interviewer` to get the list of details of all Interviewers.
2. Use `Interviewer\<InterviewerId>` to get the details of a single Interviewer.

#### DELETE
 sent `DELETE` request to `Interviewer\<InterviewerId>` to delete the records of a single Interviewer.

### Interviewee
Api for Interviewee resource is `Interviewee`
Fields for Api are 
1. name - Name of the Interviewee 
2. email - Email of the Interviewee. Unique feild, value should 
be of email format
Supported operations are `GET`,`POST`,`PUT`,`PATCH`,`DELETE`.
#### GET
1. Use `Interviewee` to get the list of details of all Interviewees.
2. Use `Interviewee\<IntervieweeId>` to get the details of a single Interviewee.

#### DELETE
 sent `DELETE` request to `Interviewee\<IntervieweeId>` to delete the records of a single Interviewee.

### Interviewer-slot
Api for Interviewer-slot resource is `interviewer-slot`
Fields for Api are 
1. interviewer - Id of the interviewer
2. available_date - available date for the Interviewer. Feild should be in the format `YYYY-MM-DD`.
3. avaliable_slots - list of available slots. refer [time slot map table](#time-slot-map-table) for getting the parameter. eg, for time slots `1 pm to 2 pm`, and `3 pm to 4 pm`. use [13,15]
available_date and interviewer is unique together. so as to avoid repetation for the same date for the same user.
Supported operations are `GET`,`POST`,`PUT`,`PATCH`,`DELETE`.
#### GET
1. Use `interviewer-slot` for getting the data of all the interviewer's avalilable slots.
2. Use `interviewer-slot/<InterviewerId>` for getting the data of a single interviewer's avalilable slots.
3. Use `interviewer-slot/<InterviewerId>/<year>` for getting the data of a single interviewer's avalilable slots in the year, `<year>`.
4. Use `interviewer-slot/<InterviewerId>/<year>/<month>` for getting the data of a single interviewer's avalilable slots in the month, `<year>/<month>`.
5. Use `interviewer-slot/<InterviewerId>/<year>/<month>/<day>` for getting the data of a single interviewer's avalilable slots in the day, `<year>/<month>/<day>`.
6. Use `interviewer-slot/0/<year>` for getting the data of all interviewer's avalilable slots in the year, `<year>`.
7. Use `interviewer-slot/<InterviewerId>/<year>/<month>` for getting the data of all interviewers avalilable slots in the month, `<year>/<month>`.
8. Use `interviewer-slot/0/<year>/<month>/<day>` for getting the data of all interviewers avalilable slots in the day, `<year>/<month>/<day>`.

Response will be in the format:
```json
[
    list of <Interviewer slots data>
]

Interviewer slots data
{
    "interviewer": {
        "id": <interviewerId>,
        "name": <interviewerName>,
        "email": <interviewerEmail>,
    },
    "avaliable_slots": [
        list of <Avaliable slots data>
    ]
}

Avaliable slots data
{
    <avaliable date>: <list of avaliable time slots in that day>
}

Example:
[
    {
        "interviewer": {
            "id": 2,
            "name": "john",
            "email": "john@john.com"
        },
        "avaliable_slots": [
            {
                "2022-03-17": [
                    15,
                    14,
                    13,
                    12,
                    10,
                    9,
                    8,
                    7
                ]
            },
            {
                "2022-03-18": [
                    19,
                    18,
                    17,
                    15,
                    14
                ]
            },
            {
                "2022-03-19": [
                    19,
                    18,
                    17,
                    15,
                    14
                ]
            }
        ]
    }
]
```
### DELETE 
1. Sent DELETE request to `interviewer-slot/<interviewerId>` to delete all records for that interviewer
2. Sent DELETE request to `interviewer-slot/<interviewerId>/<year>` to delete all records for that interviewer for year `<year>`
3. Sent DELETE request to `interviewer-slot/<interviewerId>/<year>/<month>` to delete all records for that interviewer for month `<year>/<month>`
4. Sent DELETE request to `interviewer-slot/<interviewerId>/<year>/<month>/<day>` to delete all records for that interviewer for month `<year>/<month>/<day>`.


### Interviewee-slot
Api for Interviewee-slot resource is `interviewee-slot`
Fields for Api are 
1. interviewee - Id of the interviewee
2. available_date - available date for the Interviewee. Feild should be in the format `YYYY-MM-DD`.
3. avaliable_slots - list of available slots. refer [time slot map table](#time-slot-map-table) for getting the parameter. eg, for time slots `1 pm to 2 pm`, and `3 pm to 4 pm`. use [13,15]
available_date and interviewee is unique together. so as to avoid repetation for the same date for the same user.
Supported operations are `GET`,`POST`,`PUT`,`PATCH`,`DELETE`.
#### GET
1. Use `interviewee-slot` for getting the data of all the interviewee's avalilable slots.
2. Use `interviewee-slot/<IntervieweeId>` for getting the data of a single interviewee's avalilable slots.
3. Use `interviewee-slot/<IntervieweeId>/<year>` for getting the data of a single interviewee's avalilable slots in the year, `<year>`.
4. Use `interviewee-slot/<IntervieweeId>/<year>/<month>` for getting the data of a single interviewee's avalilable slots in the month, `<year>/<month>`.
5. Use `interviewee-slot/<IntervieweeId>/<year>/<month>/<day>` for getting the data of a single interviewee's avalilable slots in the day, `<year>/<month>/<day>`.
6. Use `interviewee-slot/0/<year>` for getting the data of all interviewee's avalilable slots in the year, `<year>`.
7. Use `interviewee-slot/<IntervieweeId>/<year>/<month>` for getting the data of all interviewees avalilable slots in the month, `<year>/<month>`.
8. Use `interviewee-slot/0/<year>/<month>/<day>` for getting the data of all interviewees avalilable slots in the day, `<year>/<month>/<day>`.

Response will be in the format:
```json
[
    list of <Interviewee slots data>
]

Interviewee slots data
{
    "interviewee": {
        "id": <intervieweeId>,
        "name": <intervieweeName>,
        "email": <intervieweeEmail>,
    },
    "avaliable_slots": [
        list of <Avaliable slots data>
    ]
}

Avaliable slots data
{
    <avaliable date>: <list of avaliable time slots in that day>
}

Example:
[
    {
        "interviewee": {
            "id": 2,
            "name": "jane",
            "email": "jane@doe.com"
        },
        "avaliable_slots": [
            {
                "2022-03-19": [
                    15,
                    9,
                    8,
                    7
                ]
            }
        ]
    }
]
```
### DELETE 
1. Sent DELETE request to `interviewee-slot/<intervieweeId>` to delete all records for that interviewee
2. Sent DELETE request to `interviewee-slot/<intervieweeId>/<year>` to delete all records for that interviewee for year `<year>`
3. Sent DELETE request to `interviewee-slot/<intervieweeId>/<year>/<month>` to delete all records for that interviewee for month `<year>/<month>`
4. Sent DELETE request to `interviewee-slot/<intervieweeId>/<year>/<month>/<day>` to delete all records for that interviewee for month `<year>/<month>/<day>`.


### Find Available Slots
Api for Find Available Slots that are common for both the interviewer and interviewee is `find-available-slots`.
Supported operation is `GET`

Sent a Get request to 
```http
GET: /find-available-slots/?interviewer=<interviewerID>&interviewee=<intervieweeID>
```
Response:
```json
{
    "interviewer": "interviewerId",
    "interviewee": "intervieweeId",
    "avaliable_slots": [
        list of <Avaliable slots data>
    ]
}
Avaliable slots data
{
    <avaliable date>: <list of avaliable time slots in that day>
}

Example:
{
    "interviewer": "2",
    "interviewee": "1",
    "avaliable_slots": [
        {
            "2022-03-17": [
                "09 am to 10 am",
                "10 am to 11 am",
                "12 pm to 01 pm"
            ]
        },
        {
            "2022-03-18": [
                "02 pm to 03 pm",
                "03 pm to 04 pm",
                "05 pm to 06 pm"
            ]
        }
    ]
}
```
### Time slot map table
```
| value | time slot     |
|-------|---------------|
| 0     | 12 am to 1 am |
| 1     | 1 am to 2 am |
| 2     | 2 am to 3 am |
| 3     | 3 am to 4 am |
| 4     | 4 am to 5 am |
| 5     | 5 am to 6 am |
| 6     | 6 am to 7 am |
| 7     | 7 am to 8 am |
| 8     | 8 am to 9 am |
| 9     | 9 am to 10 am |
| 10     | 10 am to 11 am |
| 11     | 11 am to 12 pm |
| 12     | 12 pm to 1 pm |
| 13     | 01 pm to 2 pm |
| 14     | 02 pm to 3 pm |
| 15     | 03 pm to 4 pm |
| 16     | 04 pm to 5 pm |
| 17     | 05 pm to 6 pm |
| 18     | 06 pm to 7 pm |
| 19     | 07 pm to 8 pm |
| 20     | 08 pm to 9 pm |
| 21     | 09 pm to 10 pm |
| 22     | 10 pm to 11 pm |
| 23     | 11 pm to 12 am |
```

## Database Design
1. **Interviewer Table**
    __name__ - CharField
    __email__ - CharField, Unique
2. **Interviewee Table**
    __name__ - CharField
    __email__ - CharField, Unique
3. **InterviewerAvaliableTimeSlots**
    __interviewer__ - ForeignKey to interviewer
    __available_date__ - DateField
    __ipayload1__ = BigIntegerField
    __ipayload2__ = BigIntegerField
4. **IntervieweeAvaliableTimeSlots**
    __interviewee__ - ForeignKey to interviewer
    __available_date__ - DateField
    __ipayload1__ = BigIntegerField
    __ipayload2__ = BigIntegerField

### Database Explanation
The time slot for a day is a list of integers ranging from 0-23 which are distinct.
1. We are converting that interger list to 2 Integers and store it in the database. 
2. For converting the integer list to integers, we are using `convert_time_list_to_big_ints` in adaptors.py.
3. For converting back we are using `convert_big_ints_to_time_list` in adaptors.py.
This is possible because of these reasons:
- Bitlength of biggest integer in list is 5 bit, which is for 24
- Maximum number of items is 24, so that maximum amount of bitsize required is 5 x 24 = 120 bit
- BigIntegerField accounds to 64 bits, so 2 such fields are needed for storing 120 bits of data.

## Setting up the project
```
- Set up a virtual enviorment and activate
- Create a folder for cloning repo and cd into it
- git clone https://github.com/brokoder/interview-api.git
- cd interview-api/DjangoApi
- pip install -r requirements.txt
- python manage.py makemigrations InterviewApp
- python manage.py migrate InterviewApp
- python manage.py migrate
- python manage.py createsuperuser (add username, email and password)
- python manage.py drf_create_token <username> (copy the token for authentication)
- python manage.py runserver

Setting up postman
- Add "token <token generated>" for Authorization in request Header 
```

## Assumptions
1. Interview slots are of duration 1 hour.
2. Slots will begin at 0th min and not in between an hour.
3. If interviewer/interviewee is available between 7 am to 11 am, api User or front end will be able to convert that to [7,8,9,10].

## Improvements
1. Add test cases for each function.
2. Add typing for the varibles.
3. Add Docsting for the functions.
3. Create a UI template for interaction for a better User experience.
4. Make the time slots start at a any given time if needed.
5. Validate the missing error cases and sent error response.