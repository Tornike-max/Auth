from django.urls import path
from .views import RegisterView, LoginView, ForgotPasswordView, ResetPasswordView, ChangePasswordView
from django.conf import settings
from django.conf.urls.static import static
from .views import PhotoUploadView, display_uploaded_photo

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('upload-photo/', PhotoUploadView.as_view(), name='upload-photo'),
    path('display-uploaded-photo/', display_uploaded_photo, name='display-uploaded-photo'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]