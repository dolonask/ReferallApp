from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubscriberSerializer
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
        q = Subscriber.objects.get(pk=subs['subs_id'])

        serializer = SubscriberSerializer(data=subs)

        if serializer.is_valid():
            print(serializer.validated_data.get('subs_id'))
            serializer.save()

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)
