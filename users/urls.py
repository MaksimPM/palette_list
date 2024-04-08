from django.urls import path
from users.apps import UsersConfig
from users.views import UserRegister, UserAuthorizationView, PasswordRecoveryView, RequestPasswordRecoveryView

app_name = UsersConfig.name

urlpatterns = [
    path('sign-up/', UserRegister.as_view(), name='user_register'),
    path('sign-in/', UserAuthorizationView.as_view(), name='user_authorization'),
    path('recovery/', RequestPasswordRecoveryView.as_view(), name='password_recovery'),
    path('recovery/<str:hash>/', PasswordRecoveryView.as_view(), name='password_reset'),
]
