from django.urls import path
from authentication.views import authentication_user, register_user, login_user

app_name = 'authentication'

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('', authentication_user, name='authentication_user')
]