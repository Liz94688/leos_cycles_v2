from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bikes, name='all_bikes'),
    path('add_bike/', views.add_bike, name='add_bike'),
    path('edit_bike/<int:bike_id>/', views.edit_bike, name='edit_bike'),
    path('delete/<int:bike_id>/', views.delete_bike, name='delete_bike'),
]
