from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentorados, name='mentorados'),
    path('reunioes/', views.reunioes, name='reunioes')

]