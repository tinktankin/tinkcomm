from rest_framework import serializers
from app.models.subscriber import SubscriberModel

class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriberModel
        fields = ['email','first_name','last_name','full_name', 'status', 'group']
        read_only_fields = ['id', 'dateCreated', 'dateModified']

    def save(self, company):
        subscriber = SubscriberModel.objects.create(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            full_name = self.validated_data['full_name'],
            status = self.validated_data['status'],
            company = company
        )

        for obj in self.validated_data['group']:
            subscriber.group.add(obj)

        return self.validated_data
