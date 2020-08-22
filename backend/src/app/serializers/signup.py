from rest_framework import serializers

from app.models.account import AccountModel
from app.models.company import CompanyModel
from app.utils.stringutils import generate_random_string

class SignupSerializer(serializers.Serializer):
    
    company_name = serializers.CharField(max_length=225)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=225)
    last_name = serializers.CharField(max_length=225)
    password = serializers.CharField(max_length=225)
    password2 = serializers.CharField(max_length=225)

    def save(self):
        unique_code = self.get_unique_company_code()
        company = CompanyModel.objects.create(name=self.validated_data['company_name'], code=unique_code, status='ACTIVE')
        AccountModel.objects.create(
                first_name=self.validated_data['first_name'],
                status='ACTIVE',
                last_name=self.validated_data['last_name'],
                email=self.validated_data['email'],
                password=self.validated_data['password'],
                company=company
            )
        return self.validated_data

    def get_unique_company_code(self):
        random_code = generate_random_string(5)
        while True:
            try:
                CompanyModel.objects.get(code=random_code)
            except CompanyModel.DoesNotExist:
                break
        return random_code
        

