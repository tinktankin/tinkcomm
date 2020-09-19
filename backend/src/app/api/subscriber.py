from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
import pandas as pd
import numpy as np

from app.models.company import CompanyModel
from app.models.subscriber import SubscriberModel
from app.models.group import GroupModel
from app.serializers.subscriber import SubscriberSerializer
from app.utils.responseutils import send_error_response, send_success_response


# List all subscribers, or create a new subscriber
# Url: http://<your-domain>/api/v1/subscribers/
@api_view(['GET','POST'])
@permission_classes([])
@authentication_classes([])
def subscriber_list(request):

    if request.method == 'GET':
        return getAll(request)
    if request.method == 'POST':
        return create(request)

# Get, Update or Delete Subscriber By Id
# Url: http://<your-domain>/api/v1/subscribers/<pk>
# Method: GET, PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
@authentication_classes([])
def subscriber_detail(request, pk):

    subscriber = get_object(pk)
    if subscriber == None:
        return send_error_response(msg="Subscriber Not Found", code=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get(subscriber)
    if request.method == 'PUT':
        return update(request, subscriber)
    if request.method == 'DELETE':
        return destroy(subscriber)

# Upload Subscriber through CSV and EXCEL File
# Url: http://<your-domain>/api/v1/subscribers/upload
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def subscriber_upload(request):

    if request.method == 'POST':
        return upload(request)

# Get All Subscribers
def getAll(request):
    subscribers = SubscriberModel.objects.filter(company__id=request.company_id)
    serializer = SubscriberSerializer(subscribers, many=True)
    return send_success_response(msg="Subscribers Fetched successfully", payload=serializer.data)

#Create Subscriber
def create(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    subscriber = SubscriberModel(company=company)
    serializer = SubscriberSerializer(subscriber, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Subscriber Created Successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)

# Get Subscriber By Id
def get(subscriber):
    serializer = SubscriberSerializer(subscriber)
    return send_success_response(msg="Subscriber Fetched Successfully", payload=serializer.data)

# Update subscriber
def update(request, subscriber):
    serializer = SubscriberSerializer(subscriber, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="subscriber updated successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)

# Delete subscriber
def destroy(subscriber):
    subscriber.delete()
    return send_success_response(msg="Subscriber deleted successfully")

#Get Subscriber by pk
def get_object(pk=None):
    try:
        return SubscriberModel.objects.get(pk=pk)
    except SubscriberModel.DoesNotExist:
        return None

# Excel or CSV File Format
# The sequence of column should be same and as follows
# 1st Column: First Name (Mandatory Field)
# 2nd Column: Middle Name (Optional Field)
# 3rd Column: Last Name (Mandatory Field)
# 4th Column: Full Name (Optional Field)
# 5th Column: Email (Mandatory Field)
# 6th Column: Alternate Email (Optional Field)
# 7th Column: Phone Number (Optional Field, Integer Only)
# 8th Column: Alternate Phone Number (Optional Field, Integer Only)
# 9th Column: Status (Optional Field)
# 10th Column: Group (Optional Field)
# 11th Column: Company Name (Optional Field)
# 12th Column: Designation (Optional Field)
# 13th Column: City (Optional Field)
# 14th Column: Address (Optional Field)
# 15th Column: State (Optional Field)
# 16th Column: Country (Optional Field)
# 17th Column: Zip Code (Optional Field)
# 18th Column: Gender (Optional Field)
# 19th Column: Title (Optional Field)
# 20th Column: Department (Optional Field)
# 21st Column: University (Optional Field)
# 22nd Column: Degree (Optional Field)
# 23rd Column: Passing Year (Optional Field)
# 24th Column: College (Optional Field)
# 25th Column: Industry (Optional Field)
# 26th Column: Key Skills (Optional Field)
# 27th Column: Total Exp (Optional Field)
# 28th Column: Years of business (Optional Field)
# 29th Column: Turnover (Optional Field)
# 30th Column: Date of Incorporation (Optional Field)
# 31st Column: Employees (Optional Field)
# Upload Subscriber
def upload(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    input_file = request.data['file']

    if input_file.name.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.name.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    else:
        return send_error_response(msg="File Format should be CSV OR XLSX File")

    df = df.replace({np.nan: None})
    for _,column in df.iterrows():
        if not SubscriberModel.objects.filter(email=column[4]).exists():
            create_method(column, company)

        elif SubscriberModel.objects.filter(email=column[4], status="ACTIVE").exists():
            update_or_create_method(column, company)

    return send_success_response(msg="Subscriber Uploaded successfully")

def create_method(column, company):
    subscriber = SubscriberModel.objects.create(
        company=company,
        first_name=column[0],
        middle_name=column[1],
        last_name=column[2],
        full_name=column[3],
        email=column[4],
        alternate_email=column[5],
        company_name=column[10],
        designation=column[11],
        city=column[12],
        address=column[13],
        state=column[14],
        country=column[15],
        gender=column[17],
        title=column[18],
        department=column[19],
        university=column[20],
        degree=column[21],
        college=column[23],
        industry=column[24],
        key_skills=column[25],
        total_exp=column[26],
        years_business=column[27],
        turnover=column[28],
    )
    condition_check(column, subscriber, company)

    if column[8] is not None:
        subscriber.status = column[8]
    else:
        subscriber.status = "ACTIVE"

    subscriber.save()

def update_or_create_method(column,company):
    subscriber, created = SubscriberModel.objects.update_or_create(
        email=column[4],
        status="DUPLICATE",
        company=company,
        defaults=dict(
            first_name=column[0],
            middle_name=column[1],
            last_name=column[2],
            full_name=column[3],
            alternate_email=column[5],
            company_name=column[10],
            designation=column[11],
            city=column[12],
            address=column[13],
            state=column[14],
            country=column[15],
            zip_code=column[16],
            gender=column[17],
            title=column[18],
            department=column[19],
            university=column[20],
            degree=column[21],
            passing_year=column[22],
            college=column[23],
            industry=column[24],
            key_skills=column[25],
            total_exp=column[26],
            years_business=column[27],
            turnover=column[28],
        )
    )
    subscriber.group.clear()
    condition_check(column, subscriber, company)

def condition_check(column, subscriber, company):
    if column[6] is not None:
        subscriber.phone_number = int(column[6])

    if column[7] is not None:
        subscriber.alternate_phone_number = int(column[7])

    if column[16] is not None:
        subscriber.zip_code = int(column[16])

    if column[22] is not None:
        subscriber.passing_year = int(column[22])

    if column[30] is not None:
        subscriber.employees = int(column[30])

    if column[29] is not None:
        subscriber.date_of_incorporation = pd.to_datetime(column[29])

    subscriber.save()

    if column[9] is not None:
        grp_arr = column[9].split("|")
        for grp in grp_arr:
            grp_obj, created = GroupModel.objects.get_or_create(name=grp, company=company)
            subscriber.group.add(grp_obj)