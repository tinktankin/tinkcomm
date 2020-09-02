from rest_framework import serializers
from django.db import IntegrityError

from app.models.account import AccountModel
from app.models.company import CompanyModel


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=225, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = AccountModel
        fields = ['id', 'dateCreated', 'dateModified', 'first_name', 'last_name', 'email', 'status', 'gender',
                  'password', 'password2']
        read_only_fields = ['id', 'dateCreated', 'dateModified']
        extra_kwargs = {
            'gender': {'required': False},
            'password': {'write_only': True},
            'company': {'write_only': True},
        }

    def save(self, company_id):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            try:
                AccountModel.objects.create(
                    first_name=self.validated_data['first_name'],
                    status=self.validated_data['status'],
                    last_name=self.validated_data['last_name'],
                    email=self.validated_data['email'],
                    password=self.validated_data['password'],
                    company=CompanyModel.objects.get(id=company_id),
                    gender=self.validated_data['gender']
                )
            except IntegrityError:
                raise serializers.ValidationError({'email': "email already in use"})
            return self.validated_data
        else:
            raise serializers.ValidationError({'password': "passwords must match"})
    
    def update(self):
        try:
            self.instance.first_name = self.validated_data.get('first_name', self.instance.first_name)
            self.instance.last_name = self.validated_data.get('last_name', self.instance.last_name)
            self.instance.email = self.validated_data.get('email', self.instance.email)
            self.instance.status = self.validated_data.get('status', self.instance.status)
            self.instance.gender = self.validated_data.get('gender', self.instance.gender)
            self.instance.save()
            return self.instance
        except IntegrityError:
            raise serializers.ValidationError({'email': "email already in use"})