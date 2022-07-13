from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = [
    path("usuarios", views.ListUsuariosView.as_view()),
    path("usuarios/cadastro", views.CreateUsuarioView.as_view()),
    path("usuarios/<pk>", views.RetrieveUpdateDestroyUsuarioView.as_view()),
    path("login", authview.TokenObtainPairView.as_view()),
]
