from django.urls import path

from . import views

urlpatterns = [
    path('getBreadCrumbData/', views.getBreadCrumbData, name='getBreadCrumbData'),
    path('getStopEvents/', views.getCadData, name='getCadData'),
]
