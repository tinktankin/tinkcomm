from rest_framework import serializers
from app.models.subscriber import SubscriberModel

class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriberModel
        fields = ['id','full_name','first_name','middle_name','last_name','email', 'alternate_email',
                  'phone_number', 'alternate_phone_number','status', 'group', 'company_name', 'designation',
                  'city', 'address', 'state', 'country', 'zip_code', 'gender', 'title', 'department','university',
                  'degree', 'passing_year', 'college', 'industry', 'key_skills', 'total_exp', 'years_business',
                  'turnover', 'date_of_incorporation', 'employees'
                 ]
        read_only_fields = ['id', 'dateCreated', 'dateModified']
