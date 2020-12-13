from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_chart, name='view_chart'),
    path('add/<item_id>/', views.add_to_chart, name='add_to_chart'),
]
