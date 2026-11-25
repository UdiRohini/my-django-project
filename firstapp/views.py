from .models import Mobile
from .serializers import MobileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def mobileview(request, id=None):

    if request.method == 'GET':

        mobiles = Mobile.objects.all()

        serializer = MobileSerializer(mobiles, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = MobileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':

        mobile = get_object_or_404(Mobile, id=id)

        serializer = MobileSerializer(
            mobile,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        mobile = get_object_or_404(Mobile, id=id)

        mobile.delete()

        return Response({"msg": "Mobile deleted successfully"})