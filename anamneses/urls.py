from django.urls import path

from . import views

urlpatterns = [
    path("anamneses", views.ListCreateAnamneseView.as_view()),
    path("anamneses/<pk>", views.RetrieveUpdateDestroyAnamneseView.as_view()),
]
