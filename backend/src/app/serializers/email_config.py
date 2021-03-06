from rest_framework import serializers

from app.models.email_config import EmailConfigModel

class EmailConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model               = EmailConfigModel
        fields              = '__all__'
        read_only_fields    = ['id', 'dateCreated', 'dateModified']
        extra_kwargs        = {
                                'company': {'write_only': True, 'required': False},
                            }