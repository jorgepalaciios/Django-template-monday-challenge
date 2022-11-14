import os
from django.conf import settings
from django.utils.translation import ugettext as _
from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.viewsets import generics
from rest_framework import status
from utils.generators import random_string_generator
from .serializers import (
    CountryModelSerializer,
    ProvinceModelSerializer,
    CityModelSerializer,
)


class CountryCreation(APIView):
    serializer_class = CountryModelSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data['name']
        data['code']
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProvinceCreation(APIView):
    serializer_class = ProvinceModelSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data['name']
        data['country']
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class CityCreation(APIView):
    serializer_class = CityModelSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data['name']
        data['province']
        data['country']
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

