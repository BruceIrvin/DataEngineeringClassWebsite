from django.urls import path

from . import views

urlpatterns = [
    path('', views.getBreadCrumbData, name='getBreadCrumbData'),
    path('', views.getCadData, name='getCadData'),
]
