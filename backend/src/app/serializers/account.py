from rest_framework import serializers

from app.models.account import AccountModel

class AccountSerializer(serializers.ModelSerializer): 

    class Meta:
        model = AccountModel
        fields = '__all__'
        read_only_fields = ['id', 'dateCreated', 'dateModified']
        extra_kwargs = {
            'gender':       {'required': False},
            'password':     {'write_only': True},
            'company':     {'write_only': True},
        } 