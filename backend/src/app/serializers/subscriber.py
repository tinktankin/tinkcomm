from rest_framework import serializers
from app.models.subscriber import SubscriberModel

class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model               = SubscriberModel
        fields              = '__all__'
        read_only_fields    = ['id', 'dateCreated', 'dateModified']
        extra_kwargs        = {
                                'company': {'write_only': True, 'required': False},

                                'middle_name': {'required': False},
                                'full_name': {'required': False},
                                'alternate_email': {'required': False},
                                'phone_number': {'required': False},
                                'alternate_phone_number': {'required': False},
                                'status': {'required': False},
                                'group': {'required': False},
                                'company_name': {'required': False},
                                'designation': {'required': False},
                                'city': {'required': False},
                                'address': {'required': False},
                                'state': {'required': False},
                                'country': {'required': False},
                                'zip_code': {'required': False},
                                'gender': {'required': False},
                                'title': {'required': False},
                                'department': {'required': False},
                                'university': {'required': False},
                                'degree': {'required': False},
                                'passing_year': {'required': False},
                                'college': {'required': False},
                                'industry': {'required': False},
                                'key_skills': {'required': False},
                                'total_exp': {'required': False},
                                'years_business': {'required': False},
                                'turnover': {'required': False},
                                'date_of_incorporation': {'required': False},
                                'employees': {'required': False},
                            }
