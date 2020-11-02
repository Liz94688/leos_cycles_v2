from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_bike, name='add_bike')
]
