from django.urls import path
from . import views
from .chatbot import receive_message
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    #path('receive_message/', receive_message, name='receive_message'),
    path('receive_message/', views.receive_message, name='receive_message'),
    path('Settings/', views.settings, name='settings'),
    path('GradeDashboard/', views.gradeDashboard, name='GradeDashboard'),
    path('ModuleInformation/', views.moduleInformation, name='ModuleInformation'),
    path('receive_message/', receive_message, name='receive_message'),
    path('verify/', views.verify, name='verify'),
    path('getModuleInfo/', views.moduleInfo, name='getModuleInfo'),
    path('gradeInfo/', views.gradeInfo, name='gradeInfo')
]