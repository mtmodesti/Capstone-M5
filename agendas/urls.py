from django.urls import path

from . import views

urlpatterns = [
    path("agendas/", views.ListarAgendaView.as_view()),
    path("agendas/<uuid:agenda_id>/", views.RetrieveUpdateDestroyAgendaView.as_view()),
    path("agendas/medico/<uuid:medico_id>/", views.ListCreateAgendaView.as_view()),
    path("agendas/medico/<uuid:medico_id>/vago/", views.ListarHorariosVagosMedicosView.as_view()),
]
