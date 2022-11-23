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

    country = CountryModelSerializer(read_only=True)

    class Meta:
        model = Province
        fields = ['id', 'name', 'country']
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'country': {
                'required': True,
            },
        }

    def to_representation(self,instance):
        data = super().to_representation(instance)
        return data


class CityModelSerializer(serializers.ModelSerializer):

    province = ProvinceModelSerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id','name', 'province']
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

        def to_representation(self, instance):
            data = super().to_representation(instance)
            return data