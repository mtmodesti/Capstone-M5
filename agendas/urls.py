from django.urls import path

from . import views

urlpatterns = [
    path("agendas/", views.ListCreateAgendaView.as_view()),
    path("agendas/<uuid:agenda_id>", views.RetrieveUpdateDestroyAgendaView.as_view()),
]
