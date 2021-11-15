

from django.contrib import admin
from django.urls import path, include
from survey_system.api import views


urlpatterns = [
    path('api/survey', views.SurveysApiView.get_survey),
    path('api/delete_survey', views.SurveysApiView.delete_survey),
    path('api/create_survey', views.SurveysApiView.create_survey),
    path('api/delete_question', views.SurveysApiView.delete_question),
    path('api/edit_question', views.SurveysApiView.edit_question),
    path('api/edit_question', views.SurveysApiView.create_question),
    path('api/edit_survey', views.SurveysApiView.edit_survey),
    path('api/passing', views.SurveysApiView.get_passing),
    path('api/create_passing', views.SurveysApiView.create_passing),

]
