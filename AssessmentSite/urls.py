"""
URL configuration for AssessmentSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from AssessmentSite import views
from .views import MyLoginView, MyRegisterView
from django.urls import path, include

urlpatterns = [
    path('accounts/login/', MyLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register/', MyRegisterView.as_view(), name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('assessments/', include("assessments.urls")),
    path('admin/', admin.site.urls)
]
