from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    Token,
    User,
)


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'first_name': {
                'required': True,
            },
            'last_name': {
                'required': True,
            },
            'email': {
                'required': True,
            },
            'password': {
                'write_only': True,
            }
        }


class UserActivationSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=1)

    def validate_token(self, value):
        try:
            token = Token.objects.get(token=value, type=self.context['token_type'])
            self.context['token'] = token
            return value
        except (Token.DoesNotExist,):
            raise serializers.ValidationError(_('Invalid token.'))


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            self.context['user'] = user
            return value
        except (User.DoesNotExist,):
            raise serializers.ValidationError(_('Invalid email.'))


class ResetPasswordSerializer(UserActivationSerializer):
    password = serializers.CharField(min_length=6)
    confirm_password = serializers.CharField(min_length=6)

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(_('Password and confirmation not match'))
        return data
