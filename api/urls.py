from . import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverView, name="api-over-view"),
]

