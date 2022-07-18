from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = [
    path("login/", authview.TokenObtainPairView.as_view()),
    path("usuarios/", views.ListCreateUsuarioView.as_view()),
    path("usuarios/<pk>/", views.RetrieveUpdateDestroyUsuarioView.as_view()),
    path("usuario/profile/", views.ShowProfileView.as_view()),
    path("usuario/medico/criar/", views.CreateHealthAgentView.as_view()),
    path("usuario/medico/listar/", views.ListHealthAgentView.as_view()),
    path("usuario/medico/<pk>/", views.RetrieveUpdateDeleteHealthAgentView.as_view()),
    path("usuario/ativar-desativar/<pk>/", views.ChangeActivePropertyView.as_view())
]
