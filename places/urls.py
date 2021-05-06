from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_places),
    path('<int:place_id>/', views.get_place_by_id),
]
