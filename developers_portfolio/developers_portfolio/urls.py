"""developers_portfolio URL Configuration

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
from django.urls import path,include
from hire_talents import views as hire_views
from djf_surveys import views 
from django.conf import settings
from django.conf.urls.static import static

from djf_surveys.app_settings import SURVEYS_ADMIN_BASE_PATH 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hire_views.home,name='home'),
    path('developers',hire_views.display_developers,name='all_developers'),
    path('surveys/create/<str:slug>/', hire_views.CreateSurveyFormView.as_view(), name='create'),
    
    path('surveys/', include('djf_surveys.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
