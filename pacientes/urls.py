from django.urls import path

from . import views

urlpatterns = [
    path("pacientes/", views.ListCreatePacienteView.as_view()),
    path(
        "pacientes/<uuid:paciente_id>/",
        views.RetrieveUpdateDestroyPacienteView.as_view(),
    ),
    path("pacientes/todos/", views.ListAllPacientesView.as_view()),
]
