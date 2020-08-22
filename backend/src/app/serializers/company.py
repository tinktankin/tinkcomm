from rest_framework import serializers
from app.models.company import CompanyModel

class CompanySerializer(serializers.ModelSerializer): 

    class Meta:
        model = CompanyModel
        fields = '__all__'
        read_only_fields = ['id', 'dateCreated', 'dateModified'] 