
from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.catalogue, name="catalogue"),
    path("vehicule/<int:pk>/", views.vehicle_detail, name="detail"),
]
