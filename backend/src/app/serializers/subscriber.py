from rest_framework import serializers
from app.models.subscriber import SubscriberModel

class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriberModel
        fields = ['email','first_name','last_name','full_name', 'status', 'group']
        read_only_fields = ['id', 'dateCreated', 'dateModified']
