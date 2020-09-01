from rest_framework import serializers
from app.models.group import GroupModel

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupModel
        fields = ['id', 'name', 'description', 'status']
        read_only_fields = ['id', 'dateCreated', 'dateModified']

