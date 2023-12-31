from django.urls import path
from .views import RegisterView, LoginView, ForgotPasswordView, ResetPasswordView, PhotoUploadView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('upload-photo/', PhotoUploadView.as_view(), name='upload-photo'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]