from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_chart, name='view_chart')
]
