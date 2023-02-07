from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
	path('register/',userRegistrationView.as_view(), name='register'),
	path('edit-profile/',editProfileView.as_view(),name='edit-profile'),
	path('password-reset/',PasswordChangeView.as_view(), name='password-reset')
]