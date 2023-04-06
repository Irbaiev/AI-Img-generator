from django.urls import path
from . import views

from generator.views import generate_img

urlpatterns = [
    path("", views.generate_img, name="index"),
]
