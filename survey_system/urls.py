from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('survey_system.api.urls')),
]
