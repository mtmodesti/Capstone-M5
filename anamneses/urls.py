from django.urls import path

from . import views

urlpatterns = [
    path("anamneses/", views.ListAnamneseView.as_view()),
    path("anamneses/criar/<uuid:paciente_id>/", views.CreateAnamneseView.as_view()),
    path("anamneses/<pk>/", views.RetrieveUpdateDestroyAnamneseView.as_view()),
]
