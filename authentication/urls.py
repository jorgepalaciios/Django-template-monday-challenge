# base
from django.urls import path

# Auth
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
)
# others
from .views import (
    ForgotPasswordView,
    ResetPasswordView,
    UserTokenObtainPairView,
    UserRegister,
    UserActivation,
)
# from .views.change_pass_views import ResetPasswordView


app_name = 'authentication'

urlpatterns = [
    path('login/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/register/', UserRegister.as_view(), name='users_register'),
    path('users/activation/', UserActivation.as_view(), name='users_activation'),
    path('users/forgot/password/', ForgotPasswordView.as_view(), name='users_forgot_password'),
    path('users/reset/password/', ResetPasswordView.as_view(), name='reset_password'),
]