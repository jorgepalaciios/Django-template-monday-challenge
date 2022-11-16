# import os
# from django.conf import settings
from django.utils.translation import ugettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from location.models import*
from .serializers import (
    CountryModelSerializer,
    ProvinceModelSerializer,
    CityModelSerializer,
)

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    http_method_names = ['get', 'head']


class ProvinceViewSet(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceModelSerializer
    http_method_names = ['get', 'head']


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer
    http_method_names = ['get', 'head']



