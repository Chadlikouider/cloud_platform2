from django.urls import path
from esp_api import views

urlpatterns = [
    path('', views.index,name="esp_api"),
    path("receive_data/", views.receive_data, name="receice_data"),
]
