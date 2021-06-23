"""insta_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.account.api.views import RegisterApi, UserProfileView

urlpatterns = [
    # Profile
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    # path('<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    #
    path('auth/', include('djoser.urls')),
    # JWT AUTH
    path('auth/register/', RegisterApi.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
]
