from django.urls import path

from . import views

urlpatterns = [
   path("convenios/", views.CreateConvenioView().as_view()),
   path("convenios/<pk>/", views.RetrieveUpdateDestroyView().as_view()),
   path("convenio/<pk>/paciente/<paciente_id>/", views.AssociateConvenioWithPatientView.as_view()),
]
