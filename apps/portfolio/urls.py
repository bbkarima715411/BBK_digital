"""URLs de l'application portfolio."""
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="list"),
]
