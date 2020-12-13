from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_chart, name='view_chart'),
    path('add/<item_id>/', views.add_to_chart, name='add_to_chart'),
    path('adjust/<item_id>/', views.adjust_chart, name='adjust_chart'),
    path('remove/<item_id>/', views.remove_from_chart, name='remove_from_chart'),
]
