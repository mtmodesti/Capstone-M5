from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = [
    path("login/", authview.TokenObtainPairView.as_view()),
    path("usuarios/", views.ListCreateUsuarioView.as_view()),
    path("usuarios/atendentes/", views.ListUpdateAtendente.as_view()),
    path("usuarios/resumo/", views.ResumoView.as_view()),
    path("usuarios/profile/", views.ShowProfileView.as_view()),
    path("usuarios/<pk>/", views.RetrieveUpdateDestroyUsuarioView.as_view()),
    path("usuarios/medico/criar/", views.CreateHealthAgentView.as_view()),
    path("usuarios/medico/listar/", views.ListHealthAgentView.as_view()),
    path("usuarios/medico/todos/", views.ListAllHealthAgentView.as_view()),
    path("usuarios/medico/<pk>/", views.RetrieveUpdateDeleteHealthAgentView.as_view()),
    path("usuarios/ativar-desativar/<pk>/", views.ChangeActivePropertyView.as_view()),
]
