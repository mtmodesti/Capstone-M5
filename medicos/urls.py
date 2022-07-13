from django.urls import path

from . import views

urlpatterns = [
   path("medicos/", views.ShowDoctorView().as_view()),
   
]
