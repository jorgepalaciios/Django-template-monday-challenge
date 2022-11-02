from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    Country,
    Province,
    City,
)
#this is probably use later when doing serializers
""" class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'country_code': {
                'required': True,
            },
        } """

""" class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass """