from django.urls import path

from consultas import views

urlpatterns = [
    path('', views.ListConsultaView.as_view()),
    path('medico/<medico_id>/paciente/<paciente_id>/', views.CreateConsultaView.as_view()),
    path('<pk>/', views.RetrieveUpdateDestroyConsultaView.as_view())
]
