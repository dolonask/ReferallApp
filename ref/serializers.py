from rest_framework import serializers
from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

    def update(self, instance, validated_data):
        print("update")
        instance.active = validated_data.get('active', instance.active)
        return instance