from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from location.models import *


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'code': {
                'required': True,
            },
        }


class ProvinceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'country': {
                'required': True,
            },
        }


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'province': {
                'required': True,
            },
            'country': {
                'required': True,
            },
        }