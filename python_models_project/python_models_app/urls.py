from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="python_models_app")
]