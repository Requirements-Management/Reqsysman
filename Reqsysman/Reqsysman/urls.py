"""Reqsysman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from main import views
from allauth.account import views as account_views
from allauth.account.views import LoginView
from allauth.account.views import LoginView, PasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    #path('accounts/github/login/', views.github_login, name='github_login'),
    #path('accounts/', include('allauth.socialaccount.urls')),
    path('accounts/', include('allauth.urls')),
    #path('accounts/login/', LoginView.as_view(), name='account_login'),
    #path('accounts/signup/', LoginView.as_view(), name='account_signup'),
    #path('accounts/social/login/', account_views.LoginView.as_view(), name='socialaccount_login'),
    #path('accounts/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('repository/files/', views.display_repository_files, name='repository_files'),
]
