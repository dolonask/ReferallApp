from rest_framework import serializers
from .models import Subscriber, invite_statuses, Invite



class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

    def create(self, validated_data):
        return Subscriber.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.active = validated_data.get('active', instance.active)
        instance.phone = validated_data.get('phone', instance.phone)

        instance.save()
        return instance


class InviteSerializer(serializers.Serializer):
    sender = SubscriberSerializer()
    receiver = SubscriberSerializer()
    status = serializers.CharField( max_length=20, default='ACTIVE')
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)


    def create(self, validated_data):
        sender_data = validated_data.pop('sender')
        if sender_data:
            sender = Subscriber.objects.update_or_create(**sender_data)[0]
            validated_data['sender'] = sender

        receiver_data = validated_data.pop('receiver')
        if receiver_data:
            receiver = Subscriber.objects.update_or_create(**receiver_data)[0]
            validated_data['receiver'] = receiver

        #receiver = Subscriber.objects.update_or_create(**validated_data.get('receiver'))

        return Invite.objects.create(**validated_data)
