from rest_framework import serializers
from app.models.group import GroupModel

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupModel
        fields = ['name', 'description', 'status']
        read_only_fields = ['id', 'dateCreated', 'dateModified']

    def save(self, company):
        GroupModel.objects.create(
            name=self.validated_data['name'],
            description=self.validated_data['description'],
            status=self.validated_data['status'],
            company=company
        )
        return self.validated_data

