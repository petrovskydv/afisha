from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:place_id>/', views.get_place_by_id),
]
