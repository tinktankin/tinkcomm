from rest_framework import serializers

from app.models.email import EmailModel

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model               = EmailModel
        fields              = '__all__'
        read_only_fields    = ['id', 'dateCreated', 'dateModified']
        extra_kwargs        = {
                                'company': {'write_only': True, 'required': False},
                            }