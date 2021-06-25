from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubscriberSerializer, InviteSerializer
from .models import Subscriber


@api_view(['POST'])
def subscriber(request):
    #
    # {
    #     "subs_id":123,
    #     "phone":"82736482",
    #     "active":true
    # }

    if request.method == 'POST':
        subs = request.data
        subs_instance = Subscriber.objects.get(pk=subs.get('subs_id', None))

        if subs_instance:
            serializer = SubscriberSerializer(subs_instance, data=subs)
        else:
            serializer = SubscriberSerializer(data=subs)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)



    # {
    #       "sender":{
    #         "subs_id":123,
    #         "phone":"82736482"
    #       },
    #       "receiver":{
    #                    "subs_id": 123,
    #                    "phone": "82736482"
    #                }
    # }


@api_view(['POST'])
def invite(request):
    if request.method == 'POST':
        invite = request.data
        serializer = InviteSerializer(data=invite)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    return Response()