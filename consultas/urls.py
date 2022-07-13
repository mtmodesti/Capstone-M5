from django.urls import path

from .views import ListCreateConsultaView, RetrieveUpdateDestroyConsultaView

urlpatterns = [
    path('<paciente_id>/', ListCreateConsultaView.as_view()),
    path('<pk>/', RetrieveUpdateDestroyConsultaView.as_view())
]
