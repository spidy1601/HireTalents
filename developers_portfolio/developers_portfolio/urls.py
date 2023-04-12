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
    path('display',hire_views.display,name='display'),
    path('why',hire_views.why,name='why'),
    path('inquiries',hire_views.inquiries,name='inquiries'),
    path('detail/<int:pk>/',hire_views.detail,name='detail'),
    path('completed_meeting/<int:pk>/',hire_views.completed_meeting,name='completed_meeting'),
    path('searching',hire_views.searching,name='searching'),
    path('appointment_page',hire_views.appointment_page,name='appointment_page'),
    path('surveys/create/<str:slug>/', hire_views.CreateSurveyFormView.as_view(), name='create'),    
    path('surveys/', include('djf_surveys.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
