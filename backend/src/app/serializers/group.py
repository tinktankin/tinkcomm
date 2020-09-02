from rest_framework import serializers
from django.db import IntegrityError

from app.models.group import GroupModel

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model               = GroupModel
        fields              = '__all__'
        read_only_fields    = ['id', 'dateCreated', 'dateModified']
        extra_kwargs        = {
                                'company': {'write_only': True, 'required': False},
                            }
