from django.urls import path
from . import views


urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('details/<service_id>/', views.service_detail, name='service_detail'),
    path('add_level/', views.add_level, name='add_level'),
    path('add_service/', views.add_service, name='add_service'),
    path('edit_level/<int:level_id>/', views.edit_level, name='edit_level'),
    path('edit_service/<int:service_id>/', views.edit_service, name='edit_service'),
]
