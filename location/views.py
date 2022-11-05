# import os
# """ from django.conf import settings
# from django.utils.translation import ugettext as _
# from rest_framework_simplejwt.views import TokenObtainPairView
# # from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework.views import APIView
# # from rest_framework.viewsets import generics
# from rest_framework import status
# from utils.email import send_email_async
# from utils.generators import random_string_generator
# from .models import Token, TOKEN_TYPES
# from .serializers import (
#     ForgotPasswordSerializer,
#     ResetPasswordSerializer,
#     UserTokenObtainPairSerializer,
#     UserModelSerializer,
#     UserActivationSerializer,
# )


# class UserTokenObtainPairView(TokenObtainPairView):
#     serializer_class = UserTokenObtainPairSerializer


# class UserRegister(APIView):
#     serializer_class = UserModelSerializer

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         data['username'] = data['email']
#         data['is_active'] = False
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         token = random_string_generator(16, serializer.instance.username)
#         Token.objects.create(token=token, user=serializer.instance)
#         send_email_async.delay(
#             template='activate_user.html',
#             subject=_('User activation.'),
#             to=[serializer.instance.email],
#             email_data={
#                 'token': token,
#                 'user': serializer.data,
#             },
#             images=[
#                 os.path.join(settings.STATIC_ROOT, 'images', 'didox_logo.png'),
#             ]
#         )
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# class UserActivation(APIView):
#     serializer_class = UserActivationSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             data=request.data,
#             context={
#                 'token_type': TOKEN_TYPES[1][0],
#                 'request': request,
#             }
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.context['token'].user.is_active = True
#         serializer.context['token'].user.save()
#         serializer.context['token'].delete()
#         return Response(data={'message': [_('User has been activated')]})


# class ForgotPasswordView(APIView):
#     serializer_class = ForgotPasswordSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         token = random_string_generator(16, serializer.context['user'].email)
#         Token.objects.create(token=token, user=serializer.context['user'], type=TOKEN_TYPES[0][0])
#         send_email_async.delay(
#             template='reset_password.html',
#             subject=_('Reset Password.'),
#             to=[request.data.get('email')],
#             email_data={
#                 'token': token,
#                 'user': serializer.data,
#             },
#             images=[
#                 os.path.join(settings.STATIC_ROOT, 'images', 'didox_logo.png'),
#             ]
#         )
#         return Response(data={'message': [_('Recovery password email has been sended.')]})


# class ResetPasswordView(APIView):
#     serializer_class = ResetPasswordSerializer

#     def patch(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             data=request.data,
#             context={
#                 'token_type': TOKEN_TYPES[0][0],
#                 'request': request
#             }
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.context['token'].user.set_password(request.data.get('password'))
#         serializer.context['token'].user.save()
#         serializer.context['token'].delete()
#         return Response(data={'message': [_('Password updated.')]})